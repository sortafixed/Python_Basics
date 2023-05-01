class BankAccount:

    def __init__(self, balance, name):  # initialization method (parameters) id of the object is passed to self
        self.balance = balance
        self.name = name

    def credit(self, deposit):
        self.balance += deposit

    def debit(self, withdrawal):
        self.balance -= withdrawal


customer = BankAccount(0, "Rita Jones")
print(f"{customer.name}, has a balance of, {customer.balance}")
customer.credit(100)
print(f"{customer.name}, has a balance of, {customer.balance}")
customer.debit(45)
print(f"{customer.name}, has a balance of, {customer.balance}")
customer.name = "Rita Hartley"
print(f"{customer.name}, has a balance of, {customer.balance}")
