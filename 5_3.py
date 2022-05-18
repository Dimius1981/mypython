# Урок 5. Задача 3

# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

while True:
    s_name = input("Введите имя файла: ")
    if len(s_name) > 0:
        try:
            f = open(s_name, "r", encoding='utf-8')
            print(f"Файл {s_name} успешно открыт!")
            break
        except FileNotFoundError:
            print(f"Файла с именем: {s_name} не существует!")

avg_salary = 0  # Средняя зарплата сотрудников
count_person = 0  # Количество сотрудников
min_salary = 20000.0  # Минимальная зарплата

print(f"Сотрудники с зарплатой менее {min_salary} рублей:")
for line in f:
    items = line.split()
    try:
        salary = float(items[1])
        is_float = True
    except ValueError:
        is_float = False
    if items[0].istitle() and is_float:
        count_person += 1
        avg_salary += salary
    if salary < min_salary:
        print(line, end='')
f.close()

avg_salary /= count_person
print(f"Количество сотрудников всего: {count_person}")
print(f"Средняя заработная плата: {avg_salary}")
