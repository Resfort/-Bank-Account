
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

class Bank:
    def transfer(self, sender, receiver, amount):
        if amount > 0 and amount <= sender.balance:
            sender.withdraw(amount)
            receiver.deposit(amount)
            print("Перевод выполнен успешно! 💳")
        else:
            print("Ошибка перевода: недостаточно средств или неверная сумма.")

bank = Bank()
account1 = User("Алексей", 1000)
account2 = User("Мария", 500)

bank.transfer(account1, account2, 300)
bank.transfer(account1, account2, 1500)