Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s="Harishita"
type(s)
<class 'str'>
<class 'str'>
SyntaxError: invalid syntax
x="""I like momo pizza panipuri icecream and every food"""
type(x)
<class 'str'>
x='I like momo pizza panipuri icecreeam and every food'
s[0]
'H'
s[1]
'a'
s[-1]
'a'
s="This is GEC Vaishali, python Workshop."
s[0:4]
'This'
s[6:8]
's '
s[0:3]
'Thi'
s[5:7]
'is'
s[-1:-5]
''
s[-1]
'.'
s[-2:4]
''
s[-5:-1]
'shop'
s[-4:-1]
'hop'
r=Harishita
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    r=Harishita
NameError: name 'Harishita' is not defined
r="Harishita"
s="Singh"
r+s
'HarishitaSingh'
r="Harishita"
print("My name is %s",s)
My name is %s Singh
print("My name is %s",r)
My name is %s Harishita
str("This is your house")
'This is your house'
str
<class 'str'>
s="{} is a state college"
s="{} is a state college".format("GEC Vaishali")
s
'GEC Vaishali is a state college'
str="I am Harishita"
str
'I am Harishita'

# list

l=[12,"Harishita",0.7,True]
l=[3]
l[3]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    l[3]
IndexError: list index out of range
type(l)
<class 'list'>
l[1]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    l[1]
IndexError: list index out of range
l[0]
3
l[3]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    l[3]
IndexError: list index out of range
l
[3]
l=[12,"Harishita",0.7,True]
l
[12, 'Harishita', 0.7, True]
l[0]
12
l[3]
True
l.append(89)
l
[12, 'Harishita', 0.7, True, 89]
l.insert(3,67)
l
[12, 'Harishita', 0.7, 67, True, 89]
l.pop()
89
l
[12, 'Harishita', 0.7, 67, True]
l.remove(12)
l
['Harishita', 0.7, 67, True]
>>> l[2:4]
[67, True]
>>> len(l)
4
>>> max(l)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    max(l)
TypeError: '>' not supported between instances of 'float' and 'str'
>>> t=(12,"Harishita",6.8)
>>> type(t)
<class 'tuple'>
>>> t[0]
12
>>> 12
12
>>> t(count)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    t(count)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> t=(3,4,3,5,6,7,3,2,3,6,9)
>>> t.count(3)
4
>>> Days = {"MON","TUE","WED","THU"}
>>> print(Days)
{'MON', 'THU', 'WED', 'TUE'}
>>> type(Days)
<class 'set'>
>>> Days[2]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    Days[2]
TypeError: 'set' object is not subscriptable
>>> Days.add("FRI")
>>> Days
{'MON', 'THU', 'FRI', 'WED', 'TUE'}
>>> Days.discard("TUE")
>>> Days
{'MON', 'THU', 'FRI', 'WED'}
