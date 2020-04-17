 '1-2-3-4-5-6'
'1-2-3-4-5-6'
>>> ''.join(str(n) for n in range(100))
'0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899'
>>> '-'.join(str(n) for n in range(100))
'0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34-35-36-37-38-39-40-41-42-43-44-45-46-47-48-49-50-51-52-53-54-55-56-57-58-59-60-61-62-63-64-65-66-67-68-69-70-71-72-73-74-75-76-77-78-79-80-81-82-83-84-85-86-87-88-89-90-91-92-93-94-95-96-97-98-99'
>>> import timeit
>>> timeit.timeit(''-'.join(str(n) for n in range(100))')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    timeit.timeit(''-'.join(str(n) for n in range(100))')
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> timeit.timeit('"-".join(str(n) for n in range(100))')
29.842918625602508
>>> timeit.timeit('"-".join(str(n) for n in range(100))',number=10000)
0.3667644161251218
>>> timeit.timeit('"-".join[(str(n) for n in range(100)])',number=10000)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    timeit.timeit('"-".join[(str(n) for n in range(100)])',number=10000)
  File "C:\Program Files\Python36\lib\timeit.py", line 233, in timeit
    return Timer(stmt, setup, timer, globals).timeit(number)
  File "C:\Program Files\Python36\lib\timeit.py", line 123, in __init__
    compile(stmtprefix + stmt, dummy_src_name, "exec")
  File "<timeit-src>", line 2
    "-".join[(str(n) for n in range(100)])
                                        ^
SyntaxError: invalid syntax
>>> timeit.timeit('"-".join[(str(n) for n in range(100))]',number=10000)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    timeit.timeit('"-".join[(str(n) for n in range(100))]',number=10000)
  File "C:\Program Files\Python36\lib\timeit.py", line 233, in timeit
    return Timer(stmt, setup, timer, globals).timeit(number)
  File "C:\Program Files\Python36\lib\timeit.py", line 178, in timeit
    timing = self.inner(it, self.timer)
  File "<timeit-src>", line 6, in inner
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> timeit.timeit('"-".join([str(n) for n in range(100)])',number=10000)
0.23499976746637685
>>> timeit.timeit('"-".join(map(str,range(100))))',number=10000)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    timeit.timeit('"-".join(map(str,range(100))))',number=10000)
  File "C:\Program Files\Python36\lib\timeit.py", line 233, in timeit
    return Timer(stmt, setup, timer, globals).timeit(number)
  File "C:\Program Files\Python36\lib\timeit.py", line 123, in __init__
    compile(stmtprefix + stmt, dummy_src_name, "exec")
  File "<timeit-src>", line 2
    "-".join(map(str,range(100))))
                                 ^
SyntaxError: invalid syntax
>>> timeit.timeit('"-".join(map(str,range(100)))',number=10000)
0.1901711234190202
