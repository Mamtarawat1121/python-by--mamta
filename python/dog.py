class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def sound(self):
        print("Cat is meowing")

d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.sound()