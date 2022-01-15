Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> bytes(5)
b'\x00\x00\x00\x00\x00'
>>> name= 'milind'
>>> n1=bytes(name,"utf-8")
>>> n1
b'milind'
>>> num = 123
>>> n1=bytes(num)
>>> n1
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> num =[1,2,3,4]
>>> n1=bytes(num)
>>> n1
b'\x01\x02\x03\x04'
>>> n1 = bytearray(num)
>>> 
>>> b1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b1
NameError: name 'b1' is not defined
>>> n1
bytearray(b'\x01\x02\x03\x04')
>>> help("split")
No Python documentation found for 'split'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> x,y  =input("Enter values for x & y").split(" ")
Enter values for x & y12 13
>>> x
'12'
>>> y
'13'
>>> x,y  = int(input("Enter values for x & y").split(" "))
Enter values for x & y12 13
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x,y  = int(input("Enter values for x & y").split(" "))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> num=[int(i)for i in input().split(" ")]
1 2 3 4 5 6 7 8 9 12 13 11 
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    num=[int(i)for i in input().split(" ")]
  File "<pyshell#19>", line 1, in <listcomp>
    num=[int(i)for i in input().split(" ")]
ValueError: invalid literal for int() with base 10: ''
>>> [1 2 3 4 5 6 7 8 9 12 13 11 ]
SyntaxError: invalid syntax
>>> [1 2 3 4 5 6 7 8 9 12 13 11]
SyntaxError: invalid syntax
>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 11]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 11]
>>> for i in num:
	print(i, end=" ")

	
1 2 3 4 
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> flush: whether to forcibly flush the stream.
SyntaxError: invalid syntax
>>> 
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> st1="milind"
>>> for i in st1:
	print(i,end = " ")

	
m i l i n d 
>>> n = len(str1)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    n = len(str1)
NameError: name 'str1' is not defined
>>> n=len(st1)
>>> for i in range(n-1,0, -1):
	print(i,end = " ")

	
5 4 3 2 1 
>>> for i in range(n-1,0, -1):
	print(st1[i],end = " ")

	
d n i l i 
>>> for i in range(n-1,-1, -1):
	print(st1[i],end = " ")

	
d n i l i m 
>>> 