import string
import constants


class Field:
    def __init__(self, size: int, ships: int):
        self.size = size
        self.ships = ships
        self.ships_alive = ships
        self.grid = []
        for _ in range(size):
            self.grid.append([constants.EMPTY] * size)

    def display(self, show_ships=False) -> None:
        output_shift = len(str(self.size))
        line = ' ' * output_shift + ' '
        for i in range(self.size):
            line += f'{string.ascii_uppercase[i]} '
        print(line)

        for number, row in enumerate(self.grid):
            print('{:{shift}}'.format(number + 1, shift=output_shift), end=' ')
            for square in row:
                if square == constants.SHIP and show_ships:
                    print(constants.SHIP, end=' ')
                elif square == constants.SHIP:
                    print(constants.EMPTY, end=' ')
                else:
                    print(square, end=' ')
            print()
