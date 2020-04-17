#Abstract class and Inheritance

class Animal:
    def __init__(self):
        print("Animals Created")

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Dog(Animal):
    def __init__(self):
        print("Dogs Created")

    def speak(self):
        print("I am a Dog")


class Cat(Animal):
    def __init__(self):
        print("Cats Created")

    def speak(self):
        print("I am a Cat")

mydog = Dog()
mycat = Cat()


def speaking(pet):
    print(pet.speak())

mydog.speak()
