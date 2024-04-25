from python_1.tanks_game.score import Score
class Tank:
    def __init__(self, coordinates: list, direction: str, shoots: list):
        self.shoots = shoots
        self.direction = direction
        self.coordinates = coordinates
        self.score = Score()
    def info(self):
        return (f"Shots up: {self.shoots[0]}\n"
                f"Shots right: {self.shoots[1]}\n"
                f"Shots down: {self.shoots[2]}\n"
                f"Shots left: {self.shoots[3]}\n"
                f"Shots fired: {self.get_all_shots_fired()}\n"
                f"Direction: {self.direction}\n"
                f"Coordinates: {self.coordinates}\n")

    def get_all_shots_fired(self):
        result = 0
        for x in self.shoots:
            result += x
        return result
    def shoot(self, enemy_coords: list, enemy):
        if self.direction == "up":
            for x in range(self.coordinates[1], 0, -1):
                if enemy_coords[0] == self.coordinates[0] and enemy_coords[1] == x:
                    print("|| PATAIKEI ||")
                    enemy.change_location(self.coordinates)
                    self.score.count_score(100)

        if self.direction == "right":
            for x in range(self.coordinates[0], 11, 1):
                if enemy_coords[1] == self.coordinates[1] and enemy_coords[0] == x :
                    print("|| PATAIKEI ||")
                    enemy.change_location(self.coordinates)
                    self.score.count_score(100)

        if self.direction == "down":
            for x in range(self.coordinates[1], 11, 1):
                if enemy_coords[0] == self.coordinates[0] and enemy_coords[1] == x:
                    print("|| PATAIKEI ||")
                    enemy.change_location(self.coordinates)
                    self.score.count_score(100)

        if self.direction == "left":
            for x in range(self.coordinates[0], 0, -1):
                if enemy_coords[1] == self.coordinates[1] and enemy_coords[0] == x:
                    print("|| PATAIKEI ||")
                    enemy.change_location(self.coordinates)
                    self.score.count_score(100)

        self.shoots[0] += 1
        self.score.count_score(-50)

    def forward(self):
        if self.direction == "up" and self.coordinates[1] != 0:
            self.coordinates[1] -= 1
            self.score.count_score(-10)
        elif self.direction == "right" and self.coordinates[0] != 9:
            self.coordinates[0] += 1
            self.score.count_score(-10)
        elif self.direction == "down" and self.coordinates[1] != 9:
            self.coordinates[1] += 1
            self.score.count_score(-10)
        elif self.direction == "left" and self.coordinates[0] != 0:
            self.coordinates[0] -= 1
            self.score.count_score(-10)

    def backward(self):
        if self.direction == "up" and self.coordinates[1] != 9:
            self.coordinates[1] += 1
            self.score.count_score(-10)
        elif self.direction == "right" and self.coordinates[0] != 0:
            self.coordinates[0] -= 1
            self.score.count_score(-10)
        elif self.direction == "down" and self.coordinates[1] != 0:
            self.coordinates[1] -= 1
            self.score.count_score(-10)
        elif self.direction == "left" and self.coordinates[0] != 9:
            self.coordinates[0] += 1
            self.score.count_score(-10)
    def turn_left(self):
        if self.direction == "up":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "right"
        else:
            self.direction = "up"

    def turn_right(self):
        if self.direction == "up":
            self.direction = "right"
        elif self.direction == "right":
            self.direction = "down"
        elif self.direction == "down":
            self.direction = "left"
        else:
            self.direction = "up"

    def draw_tank(self):
        if self.direction == "up":
            return "^"
        elif self.direction == "right":
            return ">"
        elif self.direction == "down":
            return "v"
        elif self.direction == "left":
            return "<"

