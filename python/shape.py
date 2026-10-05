from abc import ABC, abstractmethod
def Shape(ABC):
    @abstractmethod
    def area(self):
        pass
def Circle(Shape):
    def area(self):
        print("area of circle")
        
def Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    
    def area(self):
        print("area of ractangle") 
shape = Rectangle(10,5)
shape.area()       
