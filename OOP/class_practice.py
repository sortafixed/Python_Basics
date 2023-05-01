import random


class Die:
    def __init__(self):
        self.side =0

    def throw(self):
        self.side = random.randint(1, 6)

    def get_value(self):
        return self.side


my_die = Die()
my_die.throw()
die_value = my_die.get_value()
print(f"The value thrown is: {die_value}")


