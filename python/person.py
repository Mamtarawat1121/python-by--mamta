class Person:
    def __init__(self,name ,age):
        self.__name = name
        self.__age = age
    def identity(self,name,age):
        self.__name = name
        self.__age = age
    def display_info(self):
        print(f"name is {self.__name} age is {self.__age}")
s1 = Person("mohit" , 20)
s1.identity("mohit" , 20)
s1.display_info()                 