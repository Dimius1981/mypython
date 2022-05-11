# Урок 3. Задача 3

# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def sum_two_max(var1, var2, var3):
    max1 = var1
    max2 = var2
    if var2 > max1:
        max2 = max1
        max1 = var2
    if var3 > max1:
        max2 = max1
        max1 = var3
    return max1 + max2


num1 = int(input('Первое число: '))
num2 = int(input('Второе число: '))
num3 = int(input('Третье число: '))
print(f"Сумма двух максимальных чисел = {sum_two_max(num1, num2, num3)}")
