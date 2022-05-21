# Урок 6. Задача 4

# Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат

import time


class Car:
    def __init__(self, a_color, a_name, a_police):
        self.speed = 0
        self.color = a_color
        self.name = a_name
        self.is_police = a_police

    def go(self, new_speed):
        self.speed = new_speed
        print(f"Машина {self.name} поехала!")

    def stop(self):
        self.speed = 0
        print(f"Машина {self.name} остановилась!")

    def turn(self, new_direction):
        print(f"Машина {self.name} повернула {new_direction}!")

    def show_speed(self):
        if self.speed > 0:
            print(f"Машина {self.name} едет со скоростью {self.speed} км/час.")
        else:
            print(f"Машина {self.name} стоит на месте.")


class TownCar(Car):
    speed_limit = 60

    def __init__(self, a_color, a_name):
        super().__init__(a_color, a_name, False)

    def show_speed(self):
        if self.speed > 0:
            if self.speed > TownCar.speed_limit:
                print(f"У машины {self.name} превышение скорости на {self.speed - TownCar.speed_limit} км/час!")
            else:
                print(f"Машина {self.name} едет со скоростью {self.speed} км/час.")
        else:
            print(f"Машина {self.name} стоит на месте.")


class SportCar(Car):
    def __init__(self, a_color, a_name):
        super().__init__(a_color, a_name, False)


class WorkCar(Car):
    speed_limit = 40

    def __init__(self, a_color, a_name):
        super().__init__(a_color, a_name, False)

    def show_speed(self):
        if self.speed > 0:
            if self.speed > WorkCar.speed_limit:
                print(f"У машины {self.name} превышение скорости на {self.speed - WorkCar.speed_limit} км/час!")
            else:
                print(f"Машина {self.name} едет со скоростью {self.speed} км/час.")
        else:
            print(f"Машина {self.name} стоит на месте.")


class PoliceCar(Car):
    def __init__(self, a_color, a_name):
        super().__init__(a_color, a_name, True)


town_car1 = TownCar("Синий", "Toyota Carine E")
town_car2 = TownCar("Белый", "VolksWagen Passat")

sport_car1 = SportCar("Красный", "Aston Martin")
sport_car2 = SportCar("Черный", "Audi R8")

work_car1 = WorkCar("Зеленый", "Мусоровоз")
work_car2 = WorkCar("Оранжевый", "Самосвал")

police_car1 = PoliceCar("Черно-белый", "Chevrolet Camaro")
police_car2 = PoliceCar("Черно-белый", "Dodge Charger")

town_car1.go(60)
town_car1.show_speed()
sport_car2.go(100)
sport_car2.show_speed()
time.sleep(10)

print()
town_car2.go(80)
town_car2.show_speed()
sport_car2.go(120)
sport_car2.show_speed()
town_car1.stop()
time.sleep(10)

print()
work_car1.go(40)
work_car1.show_speed()
work_car2.go(60)
work_car2.show_speed()
time.sleep(10)

print()
police_car1.go(60)
police_car1.show_speed()
police_car2.go(120)
police_car2.show_speed()
