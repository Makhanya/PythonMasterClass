class BankAccount:

    def __init__(self, owner):
        self.owner = owner
        self.bal = 0.0

    def deposit(self, amount):
        self.bal += amount
        return self.bal

    def withdraw(self, amount):
        self.bal -= amount
        return self.bal

    def balance(self):
        return self.bal


# class BankAccount:

#     def __init__(self, name):
#         self.owner = name
#         self.balance = 0.0

#     def getBalance(self):
#         return self.balance

#     def withdraw(self, amount):
#         self.balance -= amount
#         return self.balance

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance

acct = BankAccount("Darcy")
acct.owner  # Darcy
acct.balance  # 0.0
acct.deposit(10)  # 10.0
acct.withdraw(3)  # 7.0
print(acct.balance)   # 7.0
