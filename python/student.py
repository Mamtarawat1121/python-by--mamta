class Student:
    def __init__(self,name,marks):
        self.__name = name
        self.__marks = marks
    def display_info(self):
     print(f"the student name is {self.__name} , the marks is {self.__marks}")  
s1 = Student("mayank",98)
s1.display_info()

