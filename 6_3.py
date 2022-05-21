# Урок 6. Задача 3

# Реализовать базовый класс Worker (работник).
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, a_name, a_surname, a_position, a_income):
        self.name = a_name
        self.surname = a_surname
        self.position = a_position
        self._income = a_income


class Position(Worker):
    def get_full_name(self):
        return " ".join([self.name, self.surname])

    def get_total_income(self):
        return sum(self._income.values())


persons = list()
persons.append(Position("Иван", "Иванов", "Программист 1С", {"wage": 60000, "bonus": 30000}))
persons.append(Position("Петр", "Петров", "Системный администратор", {"wage": 50000, "bonus": 30000}))
persons.append(Position("Илья", "Муромец", "Служба безопасности", {"wage": 40000, "bonus": 20000}))
persons.append(Position("Ашот", "Ашотович", "Снабженец", {"wage": 30000, "bonus": 10000}))

print("Список работников с доходами:")
for i, el in enumerate(persons, 1):
    print(f"{i}) {el.get_full_name()} ({el.position}) - {el.get_total_income()} рублей")
