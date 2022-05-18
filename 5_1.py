# Урок 5. Задача 1

# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.

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
print(f"Файл {s_name} открыт для записи:")
while True:
    str_inp = input("> ")
    if len(str_inp) > 0:
        print(str_inp, file=f)
    else:
        f.close()
        print("Работа с файлом завершена")
        break