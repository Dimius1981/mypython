# Урок 2. Задача 1
# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [123, -256, 12.5, complex(5, 6), "Hello world", [1, 2, 3], (4, 5, 6),
           {'a', 'b', 'c'}, dict(kye1='1', key2='2'), True, b'text', bytearray(b"some text"), None]

for el in my_list:
    print(f"{el}: {type(el)}")
