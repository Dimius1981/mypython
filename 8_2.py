# Урок 8. Задача 2

# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyExcept(Exception):
    def __init__(self, text):
        self.text = text


a = 10
b = 0

try:
    if b == 0:
        raise MyExcept("Деление на 0!")
    else:
        c = a / b
except MyExcept as err:
    print(err)
else:
    print(f"Результат: {c}")