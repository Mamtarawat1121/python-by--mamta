
from abc import ABC, abstractmethod

# Custom Exception
class InsufficientBalanceError(Exception):
    pass


# Abstract Class
class BankAccount(ABC):

    bank_name = "Python National Bank"
    total_accounts = 0

    def __init__(self, name, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.name = name
        self.__balance = balance
        BankAccount.total_accounts += 1

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount")

        self.__balance += amount
        print(f"Deposited: Rs.{amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid withdrawal amount")

        if amount > self.__balance:
            raise InsufficientBalanceError(
                "Insufficient Balance!"
            )

        self.__balance -= amount
        print(f"Withdrawn: Rs.{amount}")

    @abstractmethod
    def calculate_interest(self):
        pass

    @classmethod
    def show_total_accounts(cls):
        print("Total Accounts:", BankAccount.total_accounts)

    @staticmethod
    def bank_info():
        print("Welcome to Python National Bank")


# Inheritance
class SavingsAccount(BankAccount):

    def calculate_interest(self):
        return self.balance * 0.04


class CurrentAccount(BankAccount):

    def calculate_interest(self):
        return 0


# Main Program
try:
    acc1 = SavingsAccount("Mamta", 10000)
    acc2 = CurrentAccount("Rahul", 20000)

    BankAccount.bank_info()

    acc1.deposit(5000)
    acc1.withdraw(3000)

    print("Name:", acc1.name)
    print("Balance:", acc1.balance)
    print("Interest:", acc1.calculate_interest())

    print("----------------")

    print("Name:", acc2.name)
    print("Balance:", acc2.balance)
    print("Interest:", acc2.calculate_interest())

    BankAccount.show_total_accounts()

except (InsufficientBalanceError, ValueError) as e:
    print("Error:", e)
