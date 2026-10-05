from abc import ABC,abstractmethod
class BankAccount:
    def deposit(self):
        print("amount")
    @abstractmethod  
    def withdraw(self):
        pass  
class SavingAccount(BankAccount):
       def withdraw(self):
           print("withdraw ammount")
s1 = SavingAccount()
s1.deposit()
s1.withdraw()           