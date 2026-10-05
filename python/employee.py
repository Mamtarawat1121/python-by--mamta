from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self,monthly_salary):
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary
c1 = PartTimeEmployee(54000)
print(c1.calculate_salary())           
    