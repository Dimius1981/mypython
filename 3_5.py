# Урок 3. Задача 5

# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
# добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.

exit_sym = 'q'
exit_flag = False

my_sum = 0

while True:
    my_str = input("Введите строку чисел через пробел: ")
    for el in my_str.split():
        # print(el)
        if el.replace("-", "").isnumeric():
            my_sum += int(el)
        if el == exit_sym:
            exit_flag = True
            break
    print(f"Сумма: {my_sum}")
    if exit_flag:
        break

