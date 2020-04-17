class Cylinder:

    #Class Object Attibute
    #V=πr2h
    #A=2πrh+2πr2
    pi =  3.14
    
    def __init__(self,radius=1,height=1):
        self.radius = radius
        self.height = height

    def volume(self):
        return Cylinder.pi*self.radius**2*self.height

    def surfacearea(self):
        return (2*Cylinder.pi*self.radius*self.height) + (2*Cylinder.pi*self.radius**2)



c = Cylinder(3,2)
print(c.volume())
print(c.surfacearea())
