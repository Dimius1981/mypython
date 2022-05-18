# Урок 5. Задача 2

# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке

# Для начала запросим у пользователя имя файла и откроем его для чтения

while True:
    s_name = input("Введите имя файла: ")
    if len(s_name) > 0:
        try:
            f = open(s_name, "r")
            print(f"Файл {s_name} успешно открыт!")
            break
        except FileNotFoundError:
            print(f"Файла с именем: {s_name} не существует!")

count_lines = 0
all_words = 0
for line in f:
    count_lines += 1
    count_word = len(line.split())
    all_words += count_word
    print(f"{count_lines}) {line.strip()} (слов: {count_word})")
f.close()

print(f"Прочитано {count_lines} строк и {all_words} слов.")
