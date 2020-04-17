x =50 

def func(x):
	print(f'the value of x is taken from global since no local is present {x}')
	x =200
	print(f'the value of x will be local variable {x}')
func(x)
