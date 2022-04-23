# Урок 1. Задаа 3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
# ввёл число 3. Считаем 3 + 33 + 333 = 369.

# Запросим число n в виде строки
num = input("Пожалуйста введите число N: ")

dbl_num = str(num) + str(num)

three_num = str(dbl_num) + str(num)

my_sum = int(num) + int(dbl_num) + int(three_num)

print(f"{num} + {dbl_num} + {three_num} = {my_sum}")
