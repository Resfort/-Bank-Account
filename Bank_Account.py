
class User:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
        else:
            print("Insufficient funds or invalid amount.")
    def get_balance(self):
        return self.__balance
    def __str__(self):
        return f"Пользователь: {self.name} | Баланс: {self.__balance} тенге."
 

class Bank:
    def transfer(self, sender, receiver, amount):
        if amount > 0 and amount <= sender.get_balance():
            sender.withdraw(amount)
            receiver.deposit(amount)
            print("Перевод выполнен успешно! 💳")
        else:
            print("Ошибка перевода: недостаточно средств или неверная сумма.")

bank = Bank()
user1 = User("Анна", 1000)
user2 = User("Иван", 500)

print(user1.get_balance())