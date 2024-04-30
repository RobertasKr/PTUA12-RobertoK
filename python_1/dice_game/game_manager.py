from python_1.dice_game.dice import Dice


class GameManager:
    def __init__(self):
        self.dices = []
        self.history = {}

    def create_dices(self, n):
        self.dices.append(Dice(n))

    def get_dices_number(self, n):
        return n

    def roll_dices(self):
        i = 1
        while i < 11:
            temp_list = []
            for x in self.dices:
                temp_list.append(x.roll_dice())
            self.history[i] = temp_list
            i += 1
        return self.history

    def input_dice_sides(self, n):
        dice_sides_count = int(input(f"Iveskite kiek sieneliu turesite {n}'am kauliukui: "))
        while True:
            if 0 < dice_sides_count <= 100:
                break
            dice_sides_count = int(input(f"Negalima virsyti 100 arba maziau 1! Ivesk s. sk. {n}'am kauliukui: "))
        return dice_sides_count

    def input_dice(self):
        dices_count = int(input("Kiek kauliuku: "))
        while True:
            if 0 < dices_count <= 5:
                break
            dices_count = int(input("Blogai ivesta reiksme!\nKiek kauliuku: "))
        return dices_count

    def create_dices_classes(self):
        dices_count = self.input_dice()
        while dices_count > 0:
            sides_count = self.input_dice_sides(dices_count)
            self.create_dices(sides_count)
            dices_count -= 1

    def main(self):
        self.create_dices_classes()
        self.roll_dices()
        print(f"\nGautas rezultatas:\n{self.history}")


game = GameManager()
game.main()
