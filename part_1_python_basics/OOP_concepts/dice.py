import random


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

    def roll_multiple(self, num_rolls):
        return [self.roll() for _ in range(num_rolls)]

    def roll_sum(self, num_rolls):
        return sum(self.roll_multiple(num_rolls))


dice = Dice()

print(dice.roll_multiple(10))
