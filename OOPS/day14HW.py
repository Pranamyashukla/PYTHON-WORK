class bankaccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount


acc1 = bankaccount("abc")
acc1.deposit(1000)
acc1.withdraw(300)
print("Account Holder:", acc1.name)
print("Balance:", acc1.balance)