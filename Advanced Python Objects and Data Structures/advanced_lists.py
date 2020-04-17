l =[12,3,4]
>>> l.sort()
>>> l
[3, 4, 12]
>>> l.reverse()
>>> l
[12, 4, 3]
>>> l.append(2)
>>> l
[12, 4, 3, 2]
>>> l.extend([1,2,3,4])
>>> l
[12, 4, 3, 2, 1, 2, 3, 4]
>>> l.pop()
4
>>> ;
SyntaxError: invalid syntax
>>> l
[12, 4, 3, 2, 1, 2, 3]
>>> l.cast()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l.cast()
AttributeError: 'list' object has no attribute 'cast'
>>> l.count(1)
1
>>> l.insert(0,3)
>>> l
[3, 12, 4, 3, 2, 1, 2, 3]
>>> list.index(2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list.index(2)
TypeError: descriptor 'index' requires a 'list' object but received a 'int'
>>> l.index(2)
4
>>> l.remove(3)
>>> l
[12, 4, 3, 2, 1, 2, 3]
