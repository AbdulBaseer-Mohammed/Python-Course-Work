s ='python programming'
s
'python programming'
s.startswith('p')
True
s.startswith("P")
False
s.startswith("pyt")
True
s.startswith("img")
False
s.startswith("ing")
False
s.endswith("img")
False
s.endswith("ing")
True
's'.islower()
True
'u'.isupper()
False
'codegnan@'.isalpha()
False
'code12'.isaplha()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    'code12'.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean '.isalpha' instead of '.isaplha'?
'code12'.isalpha()
False
'code'.isalpha()
True
'code123'.isalnum()
True
'code@123'.isalnum()
False
'code'.isalnum()
True
s
'python programming'
s.istitle()
False
'myvar'.isidentifier()
True
'my@var'.isidentifier()
False
''.isspace()
False
'        hello'.isspace()
False
'1234'.isdecimal()
True
'1234'.isdigit()
True
'1234'.isnumeric()
True
'a b c d'.split()
['a', 'b', 'c', 'd']
'a,b,c,d'.split()
['a,b,c,d']
'a,b,c,d'.split(',')
['a', 'b', 'c', 'd']
'a-b-c-d'.split('-')
['a', 'b', 'c', 'd']
'a-b-c-d'.split('-',2)
['a', 'b', 'c-d']
'a-b-c-d'.rsplit('-')
['a', 'b', 'c', 'd']
'a-b-c-d'.rsplit('-',2)
['a-b', 'c', 'd']
s="""
hello
world
python
"""
s
'\nhello\nworld\npython\n'
s.splitlines()
['', 'hello', 'world', 'python']
1=['a', 'b', 'c', 'd']
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1 =['a', 'b', 'c', 'd']
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1=['a', 'b', 'c', 'd']
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1=['a', 'b', 'c', 'd']
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=['a', 'b', 'c', 'd']
'-'.join(l)
'a-b-c-d'
'@'.join(l)
'a@b@c@d'
'*'.join(l)
'a*b*c*d'
''.join(l)
'abcd'
s
'\nhello\nworld\npython\n'
s='a-b-c-d'
s.partition('b')
('a-', 'b', '-c-d')
'python.py'.partition('.')
('python', '.', 'py')
'pyt.hon.py'.partition('.')
('pyt', '.', 'hon.py')
'pyt.hon.py'.rpartition('.')
('pyt.hon', '.', 'py')
s="hello"
s.encode()
b'hello'
t = "hello ㋡ "
t.encode()
b'hello \xe3\x8b\xa1 '
b'hello \xe3\x8b\xa1 '.decode()
'hello ㋡ '
l=[]
l=list()
l=[1,2,3]
l=list([1,2,3,4])
l
[1, 2, 3, 4]
type (l)
<class 'list'>
#mut ord dup het dyn
l=[2,3,4,5,5]
l
[2, 3, 4, 5, 5]
l=[1,1,1,1,1,1]
l
[1, 1, 1, 1, 1, 1]
l=[1,12.2,3+5j,"str",[1,2],(1,2),{1,2},{1:2},False,None]
l
[1, 12.2, (3+5j), 'str', [1, 2], (1, 2), {1, 2}, {1: 2}, False, None]
[1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
[1,2,3]*5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
l =['python','java','c','flask','fastapi','mysql','aws']
l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
l[0]
'python'
l[-1]
'aws'
l[-2]
'mysql'
l[2]
'c'
l[3]
'flask'
l[4]
'fastapi'
l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
l[:3]
['python', 'java', 'c']
l[-3:]
['fastapi', 'mysql', 'aws']
l[2:5]
['c', 'flask', 'fastapi']
l[1:2]
['java']
l[1::2]
['java', 'flask', 'mysql']
l[::2]
['python', 'c', 'fastapi', 'aws']
l[::-1]
['aws', 'mysql', 'fastapi', 'flask', 'c', 'java', 'python']
l[-3:-6:-1]
['fastapi', 'flask', 'c']
l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
'c'in l
True
'mysql' in l
True
'html' not in l
True
'css' in l
False
l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
len(l)
7
sorted(l)
['aws', 'c', 'fastapi', 'flask', 'java', 'mysql', 'python']
max(l)
"""

'python'


min(l)
'aws'
