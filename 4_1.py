# Урок 4, задача 1

# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо запускать скрипт с
# параметрами.

from sys import argv


def calc_wage(aprod, arate, aprem):
    return (aprod * arate) + aprem


try:
    production = int(argv[1])
    print(f"Выработка в часах: {production} часов")
except IndexError:
    production = 0
    print("Укажите параметр 1: выработка в часах")
except ValueError:
    production = 0
    print("Параметр 1: выработка в часах - введите целое число")

try:
    rate = int(argv[2])
    print(f"Ставка в час: {rate} тенге/час")
except IndexError:
    rate = 0
    print("Укажите параметр 2: ставка в часах")
except ValueError:
    rate = 0
    print("Параметр 2: ставка в часах - введите целое число")

try:
    premium = int(argv[3])
    print(f"Премия: {premium} тенге")
except IndexError:
    premium = 0
except ValueError:
    premium = 0
    print("Параметр 3: премия - введите целое число")

if (production > 0) and (rate > 0):
    print(f"\nЗаработная плата сотрудника: {calc_wage(production, rate, premium)} тенге")
