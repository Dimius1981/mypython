# Урок 3. Задача 2

# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.

def user_info(name, lastname, year_of_birth, city, email, phone):
    print(f"Пользователь: {name} {lastname}, {year_of_birth}-го года рождения, проживающий в городе {city}, "
          f"телефон: {phone}, email: {email}")


user_name = input("Введите имя пользователя: ")
user_lastname = input("Введите фамилию пользователя: ")
user_year = input("Введите год рождения пользователя: ")
user_city = input("Введите город проживания пользователя: ")
user_email = input("Введите email пользователя: ")
user_phone = input("Введите телефон пользователя: ")

user_info(lastname=user_lastname, name=user_name, city=user_city, phone=user_phone,
          year_of_birth=user_year, email=user_email)
