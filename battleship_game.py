from field import Field
import random
from string import ascii_uppercase
import constants
from cheat import cheat_on


class BattleshipGame:
    def __init__(self, size: int, ships: int):
        self.size = size
        self.ships = ships
        self.player_field = Field(self.size, self.ships)
        self.computer_field = Field(self.size, self.ships)

    # Это функция расстановки кораблей, она уже полностью написана
    def __place_ships_randomly(self, field: Field, num_ships: int):
        for _ in range(num_ships):
            placed = False
            while not placed:
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if self.__is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = constants.SHIP
                    placed = True

    # Это функция проверки расстановки кораблей, она уже полностью написана
    def __is_valid_ship_placement(self, field: Field, coords: tuple) -> bool:
        x, y = coords

        # Проверка на наличие соседних клеток по горизонтали и вертикали
        for j in range(-1, 2):
            for k in range(-1, 2):
                new_x, new_y = x + j, y + k
                if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == constants.SHIP:
                    return False

        return True

    def player_turn(self, x: str, y: int) -> None:
        x = ascii_uppercase.index(x)
        if self.computer_field.grid[y - 1][x] == constants.SHIP:
            self.computer_field.grid[y - 1][x] = constants.DESTROYED_SHIP
            self.computer_field.ships_alive -= 1
            print("Вы попали!")
        else:
            self.computer_field.grid[y - 1][x] = constants.MISS
            print("Промах!")

    def computer_turn(self) -> None:
        x = random.randint(0, self.player_field.size - 1)
        y = random.randint(0, self.player_field.size - 1)
        if self.player_field.grid[y][x] == constants.SHIP:
            self.player_field.grid[y][x] = constants.DESTROYED_SHIP
            self.player_field.ships_alive -= 1
            print(f"Компьютер попал по {ascii_uppercase[x]} {y + 1}")
        else:
            self.player_field.grid[y][x] = constants.MISS
            print("Компьютер промахнулся!")

    def __player_input(self) -> tuple[str, int]:
        while True:
            x = input("Введите координату по горизонтали: ").upper()
            try:
                y = int(input("Введите координату по вертикали: "))
            except ValueError:
                print("Координата по вертикали должна быть целым числом")
                continue

            if x not in ascii_uppercase[:self.size] or len(x) != 1:
                print(f"Координата по горизонтали должна быть в диапазоне от A до"
                      f" {ascii_uppercase[self.size - 1]} включительно")
            elif y <= 0 or y > self.size:
                print(f"Координата по вертикали должна быть в диапазоне от 1 до {self.size} включительно")
            elif (self.computer_field.grid[y - 1][ascii_uppercase.index(x)] == constants.DESTROYED_SHIP or
                  self.computer_field.grid[y - 1][ascii_uppercase.index(x)] == constants.MISS):
                print(f'Вы уже били по этому полю')
            else:
                return x, y

    def play(self) -> None:
        self.__place_ships_randomly(self.computer_field, self.ships)
        self.__place_ships_randomly(self.player_field, self.ships)

        is_visible = cheat_on()

        while True:
            print("Расстановка кораблей компьютера:")
            self.computer_field.display(show_ships=is_visible)

            print("Ваша расстановка кораблей:")
            self.player_field.display(show_ships=True)

            x, y = self.__player_input()
            self.player_turn(x, y)

            if self.computer_field.ships_alive <= 0:
                print("Вы победили!")
                break
            else:
                self.computer_turn()
                if self.player_field.ships_alive <= 0:
                    print("Вы проиграли!")
                    break
