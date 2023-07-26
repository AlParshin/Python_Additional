# Напишите программу, которая на вход получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию HEX используйте для проверки своего результата.

SYSTEM = 16
print('Введите число: ')
chislo_10 = int(input())

print("Результат функции 'hex' в Python = " + hex(chislo_10))
stroka_16 = []

# В этом задании рассматриваю только варианты, когда число >= 0 !
if chislo_10 == 0:
    print("Результат моей функции = 0x0")
else:
    while chislo_10 > 0:
        temp = chislo_10 % SYSTEM
        chislo_10 = chislo_10 // SYSTEM
        if temp < 10:
            stroka_16.append(temp)
        else:
            stroka_16.append(chr(temp+87))
    print("Результат моей функции = 0x", end='')
    for i in range(len(stroka_16)-1, -1, -1):
        print(stroka_16[i], end='')
