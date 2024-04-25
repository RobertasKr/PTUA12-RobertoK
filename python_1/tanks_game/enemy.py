from random import randint


class Enemy:
    def __init__(self, coordinates: list):
        self.coordinates = coordinates

    def change_location(self, tank_coordinates):
        new_coordinates = [randint(0, 9), randint(0, 9)]
        if new_coordinates[0] != tank_coordinates[0] and new_coordinates[1] != tank_coordinates[1]:
            self.coordinates = new_coordinates
