from random import randint
class Dice:
    def __init__(self, dice_sides: int):
        self.dice_sides = dice_sides

    def roll_dice(self):
        return randint(1, self.dice_sides)