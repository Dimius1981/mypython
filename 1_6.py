# Урок 1. Задача 6

# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a
# километров. Каждый день спортсмен увеличивал результат на 10% относительно
# предыдущего. Требуется определить номер дня, на который результат спортсмена составит не
# менее b километров. Программа должна принимать значения параметров a и b и выводить
# одно натуральное число — номер дня

# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км

first_day = int(input("Результат пробежки в первый день, км: "))
last_day = int(input("Желаемый результат пробежки, км: "))

count_day = 1

next_day = first_day

while next_day <= last_day:
    next_day += (next_day / 10)
    count_day += 1
    # print(f"{count_day}-й день: {next_day:.2f}")

print(f"Вы достигните результата на {count_day} день тренировок.")