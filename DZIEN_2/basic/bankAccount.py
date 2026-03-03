class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def __str__(self):
        return f"Account of {self.owner} with starting balance {self.balance}"

acc = BankAccount("Marcin",10000)
acc.deposit(2450)
acc.withdraw(1200)
print(acc)
