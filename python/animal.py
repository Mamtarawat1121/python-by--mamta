class Dog:
    def sound(self):
        print("barking")
class Cat:
    def sound(self):
        print("meow")
class Cow:
    def sound(self):
        print("mooing")
        
i= [Dog(),Cat(),Cow()] 
for val in i:
    val.sound()                       

