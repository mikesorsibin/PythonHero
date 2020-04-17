class Dog:
    def __init__(self,name):
        self.name = name
        print(self.name)
         

    def speak(self):
        return self.name + " says woof"

class Cat:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow"


mydog = Dog("Felix")
print(mydog.speak())

mycat = Cat("Smokey")
print(mycat.speak())


for pets in [mydog,mycat]:
    print(type(pets))
    print(pets.speak())


def petspeak(pet):
    print(pet.speak())

petspeak(mydog)

