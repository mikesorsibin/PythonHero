# using two tools : Returning a function and using a function as argument

def newdecorator(original_func):

    def wrap_func():
        print("some extra code to be executed before original function")
        original_func()
        print("some extra code to be executed after original function")

    return wrap_func

@newdecorator
def func_needs_decorator():
    print("I want to be decorated")

func_needs_decorator()



'''We can use @newdecorator and call the func_needs_decoroator() instead of below line
we can switch it on and off by just commenting that line
this is useful if we are referring any functions from some framework like django and python

decoratedfunction = newdecorator(func_needs_decorator)

decoratedfunction()'''


