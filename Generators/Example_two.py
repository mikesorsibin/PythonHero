'''def fibonacci(n):
    a=1
    b=1
    mylist=[]
    for i in range(n):
        mylist.append(a)
        a,b=b,a+b
    return mylist
        


for x in print(fibonacci(5)):
    print(x)'''


def fibonacci(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
        
#no need to return anything as yield will take care of it.
#to iterate over something we can use generators instead of storing it as list.

for x in fibonacci(5):
    print(x)
