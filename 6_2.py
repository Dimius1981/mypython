# Урок 6. Задача 2

# Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, length, width, m=25, h=5):
        self._length = length
        self._width = width
        self._m = m
        self._h = h

    def calc_mass(self):
        return self._width * self._length * self._m * self._h / 1000


my_length = 5000
my_width = 20
r1 = Road(my_length, my_width)
print(f"На дорогу R1 шириной {my_width} и длиной {my_length} необходимо {r1.calc_mass()} т асфальта")

my_length = 10000
my_width = 30
r2 = Road(my_length, my_width)
print(f"На дорогу R2 шириной {my_width} и длиной {my_length} необходимо {r2.calc_mass()} т асфальта")
