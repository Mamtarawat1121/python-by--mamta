def area(self):
        return self.length * self.width
class Circle:
    def __init__(self , pi , radius):
        self.pi = pi
        self.radius = radius
    def area(self):
        return self.pi * self.radius* self.radius    
s1 = Rectangle(3,5)
print(s1.area())   

s2 = Circle(3.14,2) 
print(s2.area())
