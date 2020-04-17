x =50

def printer():
	x = 25
	
	def printer1():
		print(f"My value of x is an enlcosed local {x}")
	printer1()

printer()
