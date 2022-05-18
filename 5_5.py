# Урок 5. Задача 5

# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random

# Найдем случайным образом количество чисел
num_count = random.randint(10, 100)

# сгенерируем список случайных чисел от 0 до 1000
my_list = [random.randint(0, 1000) for el in range(num_count)]

print(f"Количество чисел: {num_count}")
print(f"Список из {len(my_list)} элементов: {my_list}")

my_sum = 0
for el in my_list:
    my_sum += el
print(f"Сумма всех элементов: {my_sum}")

while True:
    s_name = input("Введите имя файла: ")
    if len(s_name) > 0:
        try:
            f = open(s_name)
            print("Файл с таким именем существует. Хотите перезаписать?")
            f.close()
            my_answer = input("Введите Да или Нет: ")
            if my_answer.upper() == "ДА":
                break
        except FileNotFoundError:
            break

f = open(s_name, "w", encoding="utf-8")
for el in my_list:
    new_str = str(el) + ' '
    f.write(new_str)
f.close()

# Откроем этот-же файл для чтения
f = open(s_name, "r", encoding='utf-8')
read_str = f.read()
f.close()

read_list = read_str.split()

read_sum = 0
for el in read_list:
    read_sum += int(el)

print(f"Считали {len(read_list)} числа, общей суммой: {read_sum}")
