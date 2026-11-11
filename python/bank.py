
class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount Deposited Successfully!")
        else:
            print("Invalid Amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Amount!")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn Successfully!")
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Available Balance:", self.__balance)


# Create Account
name = input("Enter Account Holder Name: ")
account = Bank(name, 5000)

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        amount = float(input("Enter Deposit Amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter Withdraw Amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank You for Using Our Bank!")
        break

    else:
        print("Invalid Choice! Try Again.")
