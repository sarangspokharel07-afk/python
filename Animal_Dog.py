class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
            print(self.name," is eating")

class Dog(Animal):

    def bark(self):
        print(self.name," is barking")

class Bird(Dog):

    def fly(self):
        print(self.name," is flying")


browny=Dog("Browny")
browny.eat()
browny.bark()

sparrow=Bird("Sparrow")
sparrow.eat()
sparrow.fly()