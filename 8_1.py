# Урок 8. Задача 1

# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Date:
    str_date = ""

    def __init__(self, new_date):
        Date.str_date = new_date

    @classmethod
    def str2num(cls):
        try:
            return list(map(int, cls.str_date.split('-')))
        except ValueError:
            print("Ошибка преобразования в число!")
            return None

    @staticmethod
    def check_date(num_list):
        # 0 - day
        # 1 - month
        # 2 - year

        if len(num_list) != 3:
            return False

        if num_list[2] < 0:
            return False

        if num_list[0] < 0:
            return False

        if num_list[1] in [1, 3, 5, 7, 8, 10, 12] and num_list[0] > 31:
            return False

        if num_list[1] in [4, 6, 9, 11] and num_list[0] > 30:
            return False

        if num_list[1] == 2:
            if num_list[2] % 4 == 0 and (num_list[2] % 100 != 0 or num_list[2] % 400 == 0):
                if num_list[0] > 29:
                    return False
            else:
                if num_list[0] > 28:
                    return False

        return True


date_list = ["01-01-1970", "32-01-1970", "01-02-2000", "28-02-2000", "29-02-2000", "31-03-2022", "31-04-2022",
             "32-12-2022"]


for el in date_list:
    d1 = Date(el)
    print(f"Дата \"{d1.str_date}\" является {'верной' if Date.check_date(d1.str2num()) else 'не верной'}!")
