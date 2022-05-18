# Урок 5. Задача 4

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

eng_numerals = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
rus_numerals = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]

while True:
    s_name = input("Введите имя файла: ")
    if len(s_name) > 0:
        try:
            f = open(s_name, "r", encoding='utf-8')
            print(f"Файл {s_name} успешно открыт!")
            break
        except FileNotFoundError:
            print(f"Файла с именем: {s_name} не существует!")

my_lines = f.readlines()
f.close()

new_lines = []
for el in my_lines:
    my_items = el.split()
    new_lines.append(el.replace(my_items[0], rus_numerals[eng_numerals.index(my_items[0].lower())].title()))
    print(el, end='')
print()

while True:
    s_name = input("Введите имя нового файла: ")
    if len(s_name) > 0:
        try:
            f = open(s_name)
            print(f"Файл {s_name} существует!")
            f.close()
            my_answer = input("Введите Да или Нет: ")
            if my_answer.upper() == "ДА":
                break
        except FileNotFoundError:
            break

for el in new_lines:
    print("> ", el, end='')
print()

f = open(s_name, "w", encoding='utf-8')
f.writelines(new_lines)
f.close()
