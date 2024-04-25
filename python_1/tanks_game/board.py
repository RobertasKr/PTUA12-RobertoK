from python_1.tanks_game.tank import Tank
from python_1.tanks_game.enemy import Enemy
from random import randint

tank = Tank(direction="up", coordinates=[4, 4], shoots=[0, 0, 0, 3])
enemy = Enemy(coordinates=[randint(0, 9), randint(0,9)])
def draw_board():
    for y in range(10):
        for x in range(10):
            if x == tank.coordinates[0] and y == tank.coordinates[1]:
                print(tank.draw_tank(), end="")
            elif x == enemy.coordinates[0] and y == enemy.coordinates[1]:
                print("H", end="")
            else:
                print("-", end="")
        print()


draw_board()
game_manager = input(f"Iveskite veiksma: \n")



while game_manager != "stop":
    if game_manager == "a":
        tank.turn_left()
    if game_manager == "d":
        tank.turn_right()
    if game_manager == "w":
        tank.forward()
    if game_manager == "s":
        tank.backward()
    if game_manager == "f":
        tank.shoot(enemy_coords=enemy.coordinates, enemy=enemy)
    if game_manager == "i":
        print(tank.info())

    draw_board()
    print(f"Score: {tank.score.get_score()}")
    game_manager = input(f"Type action: \n")