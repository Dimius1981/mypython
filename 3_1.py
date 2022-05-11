# Урок 3. Задача 1

# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.

def divider(var1, var2):
    try:
        return var1 / var2
    except ZeroDivisionError:
        print("Ошибка: на 0 делить нельзя!")


num1 = int(input("Введите 1-е число: "))
num2 = int(input("Введите 2-е число: "))

res = divider(num1, num2)
if res is not None:
    print(f"{num1} : {num2} = {res}")
