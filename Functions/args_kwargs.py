# * args returns a tuple. It can choose arbitary number of arguments
def myfunc(*args):
    print(args)
    print(sum(args))

myfunc(1,2,3)


# **kwargs returns a dictionary.
def myfunc1(**kwargs):
    print(kwargs)
    print("I want an {} and {}".format(kwargs['fruit'],kwargs['vegetable']))

myfunc1(fruit='apple',vegetable='onion')



#both *args and **kwargs

def myfunc2(*args,**kwargs):
    print(args)
    print(kwargs)
    print("I want {} {}".format(args[0],kwargs['food']))

myfunc2(10,20,30,food='eggs',utensil='plate')



def myfunc3(**kwargs):
    print(kwargs)
    if 'fruits' in kwargs:
        print("I want an {}".format(kwargs['fruits']))
    else:
        print("i want the other veggies {}".format(kwargs['vegetable']))
   

myfunc3(fruit='apple',vegetable='onion')
