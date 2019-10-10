import sys
import os
import stat
import shutil
from pathlib import Path
from importlib import import_module
from git import Repo

    
def remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def py_paths(root_tree, path=Path('.')):
    for blob in root_tree.blobs:
        if blob.name[-3:] == '.py':
            yield path / blob.name
    for tree in root_tree.trees:
        yield from py_paths(tree, path / tree.name)

class Solution:

    dir_name = 'clone_repo'

    def __init__(self, argv):
        self.repo = Repo.clone_from(argv[1], self.dir_name)
        self.commit = self.repo.commit(argv[2])
        self.files = list(py_paths(self.commit.tree))
        self.x = int(argv[3])

    def execute(self):
        if not self.files:
            raise Exception('File list is empty')
        for xfile in self.files:
            module = import_module('.'.join([self.dir_name] + list(xfile.parts))[:-3])
            res = module.main([xfile.name, self.x])
            del module
            yield res, xfile

    def rm_dir(self):
        for the_file in os.listdir(self.dir_name):
            file_path = os.path.join(self.dir_name, the_file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path, onerror=remove_readonly)
        


def main(argv):
    try:
        sol = Solution(argv)
        for ans in sol.execute():
            print(f'File {ans[1]} answer: {ans[0]}')
    except Exception as e:
        print(e)
    finally:
        sol.rm_dir()
   

if __name__ == '__main__':
    main(sys.argv)