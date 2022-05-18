# Урок 5. Задача 7

# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста

import json

while True:
    s_name = input("Введите имя файла: ")
    if len(s_name) > 0:
        try:
            f = open(s_name, "r", encoding='utf-8')
            print(f"Файл {s_name} успешно открыт!")
            break
        except FileNotFoundError:
            print(f"Файла с именем: {s_name} не существует!")

with open(s_name, "r", encoding='utf-8') as f_open:
    average_profit = 0
    count_firm = 0
    new_dict = {}
    for line in f_open:
        new_list = line.split()
        new_profit = int(new_list[2]) - int(new_list[3])
        new_dict.update({new_list[0]: new_profit})
        if new_profit > 0:
            average_profit += new_profit
            count_firm += 1
    profit_list = list()
    profit_list.append(new_dict)
    average_profit /= count_firm
    profit_list.append({"averge_profit": average_profit})

    with open("text_777.json", "w", encoding='utf-8') as write_f:
        json.dump(profit_list, write_f, ensure_ascii=False, indent=4)
