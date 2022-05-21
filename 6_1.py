# Урок 6. Задача 1

# Создать класс TrafficLight (светофор).
#   - определить у него один атрибут color (цвет) и метод running (запуск);
#   - атрибут реализовать как приватный;
#   - в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#   - продолжительность первого состояния (красный) составляет 7 секунд, второго
#     (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#   - переключение между режимами должно осуществляться только в указанном порядке
#     (красный, жёлтый, зелёный);
#   - проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт


import time


class TrafficLight:
    def __init__(self, red_delay=7, yellow_delay=2, green_delay=10):
        self.__states = {"Red": red_delay, "Yellow": yellow_delay, "Green": green_delay}
        self.__color = "Red"
        self.__delay = self.__states.get(self.__color)

    def running(self):
        print(self.__color)
        time.sleep(self.__delay)
        if self.__color == "Red":
            self.__color = "Yellow"
        elif self.__color == "Yellow":
            self.__color = "Green"
        else:
            self.__color = "Red"
        self.__delay = self.__states.get(self.__color)


tl1 = TrafficLight()
tl2 = TrafficLight(3, 1, 3)

print("Запускаем светофор tl1:")
c = 3
while c > 0:
    tl1.running()
    c -= 1
print("Завершаем работу tl1")

print("Запускаем светофор tl2:")
c = 3
while c > 0:
    tl2.running()
    c -= 1
print("Завершаем работу tl2")
