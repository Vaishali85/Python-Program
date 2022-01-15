Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'E:\\python 3.9.5'
>>> os.mkdir("c:/msg")
>>> os.getcwd()
'E:\\python 3.9.5'
>>> os.chdir("c://msg")
>>> os.getcwd()
'c:\\msg'
>>> os.chdir("E:\\python program")
>>> os.getcwd()
'E:\\python program'
>>> os.listdir()
['age.py', 'agrs.py', 'Assignment_1st', 'calc.py', 'demo.py', 'demo1.py', 'demo2.py', 'diamond_pattern.py', 'even.py', 'firstnamelastname.py', 'lecture practice', 'namespace_packages_demo.py', 'odd.py', 'prime.py', 'python_packages', 'spiral_matrix.txt', 'sum.py', '__pycache__']
>>> os.listdir('c:/msg')
[]
>>> os.getcwd()
'E:\\python program'
>>> os.chdir("..")
>>> os.getcwd()
'E:\\'
>>> os.rmdir('c://msg')
>>> os.rmdir('c://msg')

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    os.rmdir('c://msg')
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'c://msg'
>>> 