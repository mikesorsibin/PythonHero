'''x =50

def func():
	global x
	print(f'the value of x is taken from global since no local is present {x}')
	x =200
	print(f'the value of global variable x will be changed to local varaible value{x}')

print(x)
func()
print(x)'''



x = 50

def func(x):
    print(f'The value of x is {x} since no local variable at present')

    x = 200
    print(f"The new value of x is {x} as there is a local variable")
    print("In the next step we are returning the value of x so that we can assign the global variable value to 200 by assigning it to x")
    return x


print(x)
x = func(x)
print(f'here we are assigning the value of local x to global x by giving x = func(x) and hence the global value is {x}') 
