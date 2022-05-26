# Урок 7. Задача 2

# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, a_name, a_size):
        self.__name = a_name
        self.__v = a_size

    @property
    def consumption(self):
        return round(self.__v / 6.5 + 0.5, 2)

    def __str__(self):
        return f"Пальто \"{self.__name}\", размером: {self.__v}"

    @property
    def get_size(self):
        return self.__v


class Suit(Clothes):
    def __init__(self, a_name, a_height):
        self.__name = a_name
        self.__h = a_height

    @property
    def consumption(self):
        return self.__h * 2 + 0.3

    def __str__(self):
        return f"Костюм \"{self.__name}\", ростом: {self.__h}"

    @property
    def get_height(self):
        return self.__h


my_clothes = list()

my_clothes.append(Coat("Мужское синее", 40))
my_clothes.append(Coat("Мужское серове", 42))
my_clothes.append(Coat("Мужское черное", 43))

my_clothes.append(Suit("Спортивный синий", 40))
my_clothes.append(Suit("Мужской стильный", 42))
my_clothes.append(Suit("Водолазный оранжевый", 43))

print("Ассортимент ателье:")
for el in my_clothes:
    print(el)

print(f"\nРасход материалов")
for el in my_clothes:
    print(f"{el}, расход ткани: {el.consumption} м")

print(f"\nСуммарный расход ткани на всю одежду: {sum([el.consumption for el in my_clothes])} метра")
