# import random
# import string
# import zipfile
#
#
# # Функция для генерации случайной строки
# def generate_random_string(length):
#     characters = string.ascii_letters + string.digits
#     return ''.join(random.choice(characters) for _ in range(length))
#
#
# # Генерация списка строк
# random_strings = [generate_random_string(100) for _ in range(10000)]
#
# # Запись строк в файл
# with open('text.txt', 'w') as file:
#     for line in random_strings:
#         file.write(line + '\n')
#
# # Архивация файла
# with zipfile.ZipFile('text.zip', 'w') as zip_file:
#     zip_file.write('text.txt')
#
# print("Программа выполнена успешно!")


import zipfile
from collections import Counter
import re

# Шаг 2: Распаковка ZIP-файла
with zipfile.ZipFile('text.zip', 'r') as zip_ref:
    zip_ref.extractall()

# Шаг 3: Чтение файла и вывод строк на экран
with open('text.txt', 'r') as file:
    lines = file.readlines()
    print("Вывод всех строк:")
    for line in lines:
        print(line.strip())  # strip() для удаления переносов строк

# Шаг 4: Подсчет частоты символов
all_text = ''.join(lines).lower()  # Преобразуем в нижний регистр для единообразия
char_frequency = Counter(all_text)

# Шаг 5: Вывод 5 самых повторяющихся символов
most_common_chars = char_frequency.most_common(5)
print("\n5 самых часто встречающихся символов и их количество:")
for char, count in most_common_chars:
    print(f"{char}: {count}")