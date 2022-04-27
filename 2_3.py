# Урок 2. Задача 3

# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

# Создадим кортеж сезонов
# indexes:    0          1         2         3
seasons = ("winter", "spring", "summer", "autumn")

month_list = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 0]

month_dict = {0: 0, 1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 3, 9: 3, 10: 3, 11: 0}

while True:
    my_month = int(input("Введите месц (1..12): "))
    if my_month >= 1 and my_month <= 12:
        break

print(f"list: Месяц {my_month} относится к сезону \"{seasons[month_list[my_month-1]]}\"")

print(f"dict: Месяц {my_month} относится к сезону \"{seasons[month_dict.get(my_month-1)]}\"")
