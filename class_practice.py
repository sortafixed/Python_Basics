import random


class Die:
    def __init__(self):
        self.side = 0

    def throw(self, number_of_throws):
        i = 0
        while i < number_of_throws:
            self.side = random.randint(1, 6)
            print(self.side)
            i += 1


throws = 0
throws = int(input("Enter the number of throws: "))

my_die = Die()
my_die.throw(throws)

