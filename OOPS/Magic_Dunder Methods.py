class Sample:
    def __init__(self,name,place,age):
        self.name = name
        self.place = place
        self.age =age

    def __str__(self):
        return f"My name is {self.name} and i live in {self.place}"

    def __len__(self):
        return self.age

    def __del__(self):
        print("The details are deleted")


s = Sample('mike','chennai',26)
print(s)
print(len(s))
del(s)
