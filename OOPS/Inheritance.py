class Animal:
    def __init__(self):
        print("Animals Created")

    def speak(self):
        print("I am an Animal")


class Dogs(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dogs Created")

    def bark(self):
        print("Woof")

mydog = Dogs()
mydog.speak()
mydog.bark()
