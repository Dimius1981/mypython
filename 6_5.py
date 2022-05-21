# Урок 6. Задача 5

# Реализовать класс Stationery (канцелярская принадлежность).
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра

class Stationery:
    def __init__(self, a_title):
        self.title = a_title

    def drow(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def drow(self):
        print(f"Ручка {self.title} рисует")


class Pencil(Stationery):
    def drow(self):
        print(f"Карандаш {self.title} рисует")


class Handle(Stationery):
    def drow(self):
        print(f"Маркер {self.title} рисует")


pen1 = Pen("шариковая")
pen2 = Pen("гелевая")

pencil1 = Pencil("простой")
pencil2 = Pencil("красный")

handle1 = Handle("черный")
handle2 = Handle("синий")

pen1.drow()
pen2.drow()
pencil1.drow()
pencil2.drow()
handle1.drow()
handle2.drow()
