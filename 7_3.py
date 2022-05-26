# Урок 7. Задача 3

# Реализовать программу работы с органическими клетками, состоящими из ячеек

import random

class Cell:
    def __init__(self, a_col):
        self.__col = a_col

    def __add__(self, other):
        return Cell(self.__col + other.__col)

    def __sub__(self, other):
        if self.__col >= other.__col:
            return Cell(self.__col - other.__col)
        else:
            return "Недостаточно ячеек для вычитания!"

    def __mul__(self, other):
        return Cell(self.__col * other.__col)

    def __truediv__(self, other):
        try:
            return Cell(self.__col // other.__col)
        except ZeroDivisionError:
            return "На 0 делить нельзя!"

    def __str__(self):
        return str(self.__col)

    def make_order(self, col_cells):
        if self.__col >= col_cells:
            print('\n'.join(['*' * col_cells for el in range(self.__col // col_cells)]))
        if self.__col % col_cells > 0:
            print(f"{'*' * (self.__col % col_cells)}")


my_cells = [Cell(random.randint(0, 20)) for el in range(10)]

print(', '.join(map(str, my_cells)))

print(f"\nCell({my_cells[0]}) + Cell({my_cells[1]}) = Cells({my_cells[0] + my_cells[1]})")

print(f"\nCell({my_cells[2]}) - Cell({my_cells[3]}) = Cells({my_cells[2] - my_cells[3]})")

print(f"\nCell({my_cells[4]}) * Cell({my_cells[5]}) = Cells({my_cells[4] * my_cells[5]})")

print(f"\nCell({my_cells[6]}) / Cell({my_cells[7]}) = Cells({my_cells[6] / my_cells[7]})")

print(f"Cell({my_cells[0]}).make_order(5)")
my_cells[0].make_order(5)
