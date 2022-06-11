# Урок 8. Задача 7

# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class MyComplex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} + i{self.b}"

    def __add__(self, other):
        return MyComplex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return MyComplex(self.a * other.a, self.b * other.b)


cpl1 = MyComplex(1, 2)
cpl2 = MyComplex(5, 6)

print(f"cpl1 = {cpl1}")
print(f"cpl2 = {cpl2}")

print(f"\ncpl1 + cpl2 = {cpl1 + cpl2}")
print(f"cpl1 * cpl2 = {cpl1 * cpl2}")
