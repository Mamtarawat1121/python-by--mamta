class BankAccount:
 def __init__(self, balance):
     self.__balance = balance
 def deposit(self,amount):
     self.__balance += amount
 def withdraw(self,amount):
     self.__balance -= amount
 def display_balance(self):
     print("balance is ", self.__balance)
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
account.display_balance()        