# Создайте функцию, которая создает файлы с указанным расширением. Функция принимает следующие параметры:
#  - расширение;
#  - минимальная длина случайно сгенерированного имени, по умолчанию 6;
#  - максимальная длина случайно сгенерированного имени, по умолчанию 30;
#  - минимальное число случайных байт, записанных в файл, по умолчанию 256;
#  - максимальное число случайных байт, записанных в файл, по умолчанию 4096;
#  - количество файлов, по умолчанию 42;
# Имя файла и его размер должны быть в рамках переданного диапазона.

import random
import string
import os

MIN_LENGTH = 6
MAX_LENGTH = 30
MIN_SIZE = 256
MAX_SIZE = 4096
QUANTITY = 42
PATH = "D:/TEST/Python_Additional/files_seminar_7/"


def createFile():
    for i in range(QUANTITY):
        print(f"Создание {i+1}го файла:")
        rand = generateRandomString(MIN_LENGTH, MAX_LENGTH)
        text = generateRandomString(
            random.randint(1, 10), random.randint(10, 500))
        while True:
            file = open(f"{PATH}{rand}.{file_extension}", "a")
            file.write(text + ' ')
            file.close()
            print(os.path.getsize(f"{PATH}{rand}.{file_extension}"), end='')
            print(" байт")
            if (os.path.getsize(f"{PATH}{rand}.{file_extension}") >= MIN_SIZE) and (os.path.getsize(f"{PATH}{rand}.{file_extension}") <= MAX_SIZE):
                break
            elif (os.path.getsize(f"{PATH}{rand}.{file_extension}") > MAX_SIZE):
                file = open(f"{PATH}{rand}.{file_extension}", "a")
                file.truncate(MAX_SIZE)
                break
        file.close()


def generateRandomString(MIN_LENGTH, MAX_LENGTH):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters)
                            for _ in range(MIN_LENGTH, MAX_LENGTH))
    return random_string


print("Введите расширение для файлов (например: txt)")
file_extension = str(input())
createFile()
