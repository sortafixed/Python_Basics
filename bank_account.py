class BankAccount:

    def __init__(self, balance, name):  # initialization method (parameters) id of the object is passed to self
        self.balance = balance
        self.name = name

    def credit(self, deposit):
        self.balance += deposit

    def debit(self, withdrawal):
        self.balance -= withdrawal

    def get_balance(self):  # getter method
        return self.balance

    def get_name(self):
        return self.name

    def set_name(self, name): # setter method
        self.name = name


customer = BankAccount(0, "Rita Jones")
print(f"{customer.get_name()}, has a balance of, {customer.get_balance()}")
customer.credit(100)
print(f"{customer.get_name()}, has a balance of, {customer.get_balance()}")
customer.debit(45)
print(f"{customer.get_name()}, has a balance of, {customer.get_balance()}")
customer.set_name("Rita Hartley")
print(f"{customer.get_name()}, has a balance of, {customer.get_balance()}")
