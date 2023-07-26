# Напишите программу, которая принимает две строки вида "a/b" - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

print("Введите первую дробь в формате 'a/b': ")
str_1 = (input())
print("Введите вторую дробь в формате 'a/b': ")
str_2 = (input())
str_1_split = str_1.split('/')
str_2_split = str_2.split('/')
a1 = float(str_1_split[0])
b1 = float(str_1_split[1])
a2 = float(str_2_split[0])
b2 = float(str_2_split[1])
multi_chisliteley = a1 * a2
multi_znamenateley = b1 * b2
print('Произведение дробей = ', multi_chisliteley / multi_znamenateley)
print('Произведение дробей (через Fraction) = ',
      float(Fraction(str_1)*Fraction(str_2)))
if b1 != b2:
    a1 = a1 * b2
    a2 = a2 * b1
    b1 = b1 * b2
sum_chisliteley = a1 + a2
multi_chisliteley = a1 * a2
multi_znamenateley = b1 * b2
print('Сумма дробей = ', sum_chisliteley / b1)
print('Сумма дробей (через Fraction) = ',
      float(Fraction(str_1)+Fraction(str_2)))
