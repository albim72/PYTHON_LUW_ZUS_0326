class InsufficientFundsError(Exception):
    pass

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Brak wystarczającch środków...")
        self.balance -= amount
        print(f"wypłata wykonana, nowe saldo: {self.balance}")


acc = BankAccount(10000)
try:
    acc.withdraw(100)
except InsufficientFundsError as e:
    print(e)
