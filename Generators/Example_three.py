def myfunc():
    for x in range(3):
        yield x

x = myfunc()

#using next to call the values of x one by one
print(next(x))


#iter keyword

s="hello"

for x in s:
    print(x)

#here we cannot directly call next method, we need to iter s.

iter_s = iter(s)

print(next(iter_s))
