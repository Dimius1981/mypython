# Урок 7. Задача 1 (вариант 2)

# В этом варианте я использовал comprehension в методе __add__

# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.

class Matrix:
    def __init__(self, new_lists):
        self.__my_list = new_lists
        self.__my_rows = len(self.__my_list)
        self.__my_cols = len(self.__my_list[0])
        # print(f"Размерность матрицы: {self.__my_rows} х {self.__my_cols}")

    def __str__(self):
        __my_str = ""
        for row in self.__my_list:
            __my_str += str(row) + "\n"
        return __my_str

    def __add__(self, other):
        __sum_list = list()
        if ((self.__my_cols == other.__my_cols) and
           (self.__my_rows == other.__my_rows)):
            return Matrix([[self.__my_list[row][col] + other.__my_list[row][col] for col in range(self.__my_cols)] for row in range(self.__my_rows)])
        else:
            return "Размерности матриц не совпадают!"


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
m3 = Matrix([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])

print(f"Матрица m1:")
print(m1)
print()

print(f"Матрица m2:")
print(m2)
print()

print(f"Сумма матриц m1 + m2:")
print(m1 + m2)
print()

print(f"Матрица m1:")
print(m1)
print()

print(f"Матрица m3:")
print(m3)
print()

print(f"Сумма матриц m1 + m3:")
print(m1 + m3)
print()

print(f"Сумма матриц m1 + m2 + m1:")
print(m1 + m2 + m1)
