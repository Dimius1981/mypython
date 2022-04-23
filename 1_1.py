# Урок 1. Задача 1
# Поработайте с переменными, создайте несколько, выведите на экран. Запросите у
# пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

# Умный калькулятор 1.0

print("Привет! Я умный калькулятор. Давай поиграем...\n")

name = input("Скажи, как тебя зовут? ")

print("Какое красивое имя:", name, "\n")

print("Я умею складывать и вычитать числа, а также умножать и делить их.\n")

print("Что ты хочешь? Выбери:")
print("  1 - сложить")
print("  2 - вычесть")
print("  3 - умножить")
print("  4 - разделить")
my_oper = int(input("Твой выбор: "))

number_a = int(input("\nТеперь введи первое число: "))

number_b = int(input("и второе число: "))

result_c = 0

if my_oper == 1:
    result_c = number_a + number_b
elif my_oper == 2:
    result_c = number_a - number_b
elif my_oper == 3:
    result_c = number_a * number_b
elif my_oper == 4:
    if number_b > 0:
        result_c = number_a / number_b
    else:
        print("Ой, на 0 делить нельзя!\n")
else:
    print("Интересно, что ты задумал?...\n")

print("Получим результат: ", result_c)

print("\nНу все", name, "мне пора идти. Пока.")
