# Урок 3. Задача 5

# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
# добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.
def str2num(astr):
    if astr.isnumeric():
        return int(astr)
    return 0


def sumstrsplit(astr):
    cur_sum = 0
    for el in astr.split():
        cur_sum += str2num(el)
        if el == exit_sym:
            return cur_sum, True  # return sum, exit_flag
    return cur_sum, False  # return sum, exit_flag


exit_sym = 'q'
exit_flag = False

my_sum = 0

while True:
    my_str = input("Введите строку чисел через пробел: ")
    str_sum, exit_flag = sumstrsplit(my_str)
    my_sum += str_sum
    print(f"Сумма: {my_sum}")
    if exit_flag:
        break

