# Python Git Test Task

A Python application that clones a remote git repository into a workspace directory, evaluates the containing python files with a number parameter x, prints the result and cleans up the working directory.

## Prerequisites

Application needs `Python 3`, `pip` and `git` executable to be installed on the system. 

## Installing

Clone this repository to begin:
```
git clone https://github.com/strange012/python_git_test_task
```
Install requirements from the file:
```
py -m pip install requirements.txt
```

## Usage

Run the application via `Python 3` executable with 3 parameters:
* Remote repository link
* Commit reference
* Numeric variable _x_
### Example 1:
```
py -m solution https://github.com/strange012/test_git_test HEAD~0 10
```
Which outputs:
```
File fib.py answer: 55
File module\cube.py answer: 1000
```
### Example 2:
```
py -m solution https://github.com/strange012/test_git_test HEAD~2 15
```
Which outputs:
```
File fib.py answer: 610
```
