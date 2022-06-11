# Урок 8. Задача 4, 5, 6

# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
# оргтехники на склад и передачу в определённое подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру (например, словарь).

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from abc import ABC, abstractmethod


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


# Объект склада оргтехники
# Содержит параметр size - вместимость склада (больше этого значения нельзя будет поместить оборудования на склад)
# Объект склада содержи список словарей офисной техники
#
# Список офисной техники содержит словари вида: {'obj': obj_by_OfficeEquipment, 'cnt': number}
#   obj_by_OfficeEquipment - экземпляр объекта потомка от OfficeEquipment
#   number - количество штук данного вида офисной техники
class StockEquipment:
    def __init__(self, size):
        self.size = size     # Вместимость склада
        self.list_item = []  # Список словарей оборудования

    def get_count(self):
        return len(self.list_item)

    def add_item(self, item):
        if item is not None:
            if self.get_count() < self.size:
                self.list_item.append(item)
            else:
                raise OwnError("Не возможно добавить объект! На складе нет места!")

    def del_item(self, item):
        if self.list_item.count(item) > 0:
            self.list_item.remove(item)
        else:
            raise OwnError("Не возможно списать объект! Склад пустой!")

    def view_items(self):
        for idx, item in enumerate(self.list_item, 1):
            print(f"{idx:4} | {item}")

    def pop_item(self, **kwparams):
        if (len(kwparams) > 0):
            if kwparams.get('idx') in range(self.get_count()):
                return self.list_item.pop(kwparams.get('idx'))
            elif len(kwparams.get('name')) > 0:
                for idx, el in enumerate(self.list_item):
                    if el.name.find(kwparams.get('name')) > -1:
                        return self.list_item.pop(idx)
            else:
                return None
        else:
            return None



class OfficeEquipment(ABC):
    def __init__(self, a_name, a_brand, a_price):
        self.name = a_name
        self.brand = a_brand
        self.price = a_price

    @abstractmethod
    def __str__(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, a_name, a_brand, a_price, a_type_printer):
        super().__init__(a_name, a_brand, a_price)
        self.type_printer = a_type_printer

    def __str__(self):
        return f"Принтер: {self.brand:10} {self.name + ' (' + self.type_printer + ')':40} цена: {self.price:6} тг"


class Scanner(OfficeEquipment):
    def __init__(self, a_name, a_brand, a_price, a_type_scanner):
        super().__init__(a_name, a_brand, a_price)
        self.type_scanner = a_type_scanner

    def __str__(self):
        return f"Сканер : {self.brand:10} {self.name + ' (' + self.type_scanner + ')':40} цена: {self.price:6} тг"


class Xerox(OfficeEquipment):
    def __init__(self, a_name, a_brand, a_price):
        super().__init__(a_name, a_brand, a_price)

    def __str__(self):
        return f"Ксерокс: {self.brand:10} {self.name:40} цена: {self.price:6} тг"


# Создадим склад на 10 позиций
my_stock = StockEquipment(10)

# Добавим в него офисную технику
my_stock.add_item(Printer('Neverstop', 'HP', 93990, 'лазерный'))
my_stock.add_item(Printer('L121 A4', 'Epson', 79990, 'струйный'))
my_stock.add_item(Printer('Europe 107a', 'HP', 62990, 'лазерный'))
my_stock.add_item(Scanner('ImageFORMULA DRC225II', 'Canon', 149990, 'протяжный'))
my_stock.add_item(Scanner('Workforce DS5500N', 'Epson', 922650, 'планшетный'))
my_stock.add_item(Scanner('SP1130N', 'Fujitsu', 282266, 'протяжный с АПД'))
my_stock.add_item(Xerox('Laser Jet PRO MFP M28a', 'HP', 71990))
my_stock.add_item(Xerox('MF3010', 'Canon', 214990))
my_stock.add_item(Xerox('Laser 137fnw', 'HP', 100990))
my_stock.add_item(Xerox('Laser 135a', 'HP', 86990))

# Выведем список офисной техники
print("Список офисной техники на складе:")
my_stock.view_items()

print()
print("Попытаемся добавить еще один объект на склад:")
try:
    my_stock.add_item(Printer('Neverstop-2', 'HP', 113990, 'лазерный'))
except OwnError as err:
    print(err)

# Создадим склад подразделения и переместим в этот склад несколько позиций оргтехники
my_subdiv = StockEquipment(5)

print("\nПеренесем запись с индексом 0 со склада в другое подразделение")
my_subdiv.add_item(my_stock.pop_item(idx=0))

print("\nСклад подразделения:")
my_subdiv.view_items()

print("\nПеренесем объект с именем содержащем текст \"Laser Jet\" в другое подразделение")
my_subdiv.add_item(my_stock.pop_item(name='Laser Jet'))

print("\nСклад подразделения:")
my_subdiv.view_items()

print("\nСписок офисной техники на складе:")
my_stock.view_items()
