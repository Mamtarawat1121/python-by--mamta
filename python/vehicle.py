from abc import ABC , abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def Start(self):
        print("vehicle is starting")
class Car(Vehicle):
    def Start(self):
        print("car is starting")        
class Bike(Vehicle):
    def Start(self):
        print("bike is starting")
c1 = Car()
c1.Start()
b1 = Bike()
b1.Start()        

        