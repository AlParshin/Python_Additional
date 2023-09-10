# Напишите программу, которая на вход получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию HEX используйте для проверки своего результата.

import logging

logging.basicConfig(level=logging.INFO, filename="Task_2.log", filemode="a",
                    encoding="UTF-8", format="%(asctime)s %(levelname)s %(message)s")

SYSTEM = 16
print('Введите число: ')
chislo_10 = int(input())

logging.info(f"Введенное входное значение для хэширования: {chislo_10}")

logging.info(
    "Результат, рассчитанный силами встроенной функции 'hex' в Python = " + hex(chislo_10))
stroka_16 = []
final_str = ""

# В этом задании рассматриваю только варианты, когда число >= 0 !
if chislo_10 == 0:
    logging.info("Результат пользовательской функции = 0x0")
else:
    while chislo_10 > 0:
        temp = chislo_10 % SYSTEM
        chislo_10 = chislo_10 // SYSTEM
        if temp < 10:
            stroka_16.append(temp)
        else:
            stroka_16.append(chr(temp+87))
    final_str += "Результат пользовательской функции = 0x"
    for i in range(len(stroka_16)-1, -1, -1):
        final_str += str(stroka_16[i])
    logging.info(final_str)
logging.info("---")
