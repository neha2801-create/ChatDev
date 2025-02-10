import secrets

class Dice:
    def __init__(self, num_sides):
        self.num_sides = num_sides
    def roll(self):
        return secrets.SystemRandom().randint(1, self.num_sides)
