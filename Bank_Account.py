
class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient funds or invalid amount.")