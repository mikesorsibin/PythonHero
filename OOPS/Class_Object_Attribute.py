class circle():
    #class object attribute
    pi = 3.14

    def __init__ (self,radius=1):
        self.myradius = radius

    #Method
    def getcircumference(self):
        return self.myradius * circle.pi * 2


mycircle = circle(radius=30)

print(mycircle.myradius)#attibutes

print(mycircle.getcircumference())#methods
