class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print("Current Balance:", self.balance)


account = Bank("Mamta", 5000)

account.deposit(2000)
account.withdraw(1000)
account.check_balance()