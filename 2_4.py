# Урок 2. Задача 4

# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
# слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только
# первые 10 букв в слове.

my_str = input("Введите строку разделяя слова пробелами: ")

for idx, el in enumerate(my_str.split()):
    print(f"{idx}: строка = \"{el[:10]}\"")
