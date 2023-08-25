# Напишите программу, которая принимает две строки вида "a/b" - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.
# Реализуйте с помощью классов!

from fractions import Fraction


class Drobi:
    def __init__(self, numerator: float, denominator: float) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def print_drob(self):
        print("Числитель = ", self.numerator)
        print("Знаменатель = ", self.denominator)


def multi_Drobi(a1, a2, b1, b2):
    multi_chisliteley = a1 * a2
    multi_znamenateley = b1 * b2
    print('Произведение дробей = ', multi_chisliteley / multi_znamenateley)
    if b1 != b2:
        a1 = a1 * b2
        a2 = a2 * b1
        b1 = b1 * b2


def poisk_naimenshego_kratnogo(b1, b2):
    if b1 == 0 or b2 == 0:
        return 0
    else:
        return abs(b1 * b2) // sokrashenie_drobi(b1, b2)


def sokrashenie_drobi(b1, b2):
    while b2:
        b1, b2 = b2, b1 % b2
    return b1


def sum_Drobi(a1, a2, b1, b2):
    common_denominator = poisk_naimenshego_kratnogo(b1, b2)
    a1 *= common_denominator // b1
    b1 = common_denominator
    a2 *= common_denominator // b2
    b2 = common_denominator
    sum_chisliteley = a1 + a2
    divisor = sokrashenie_drobi(sum_chisliteley, common_denominator)
    sum_chisliteley //= divisor
    common_denominator //= divisor
    print('Сумма дробей = ', sum_chisliteley / common_denominator)


print("-------------------------------------------------")
print("Введите первую дробь в формате 'a/b': ")
d_1 = (input())
print("-------------------------------------------------")
print("Введите вторую дробь в формате 'a/b': ")
d_2 = (input())
print("-------------------------------------------------")
d_1_split = d_1.split('/')
d_2_split = d_2.split('/')

drob_1 = Drobi(float(d_1_split[0]), float(d_1_split[1]))
drob_2 = Drobi(float(d_2_split[0]), float(d_2_split[1]))

print("Параметры первой дроби:")
drob_1.print_drob()
print("-------------------------------------------------")
print("Параметры второй дроби:")
drob_2.print_drob()
print("-------------------------------------------------")

multi_Drobi(drob_1.numerator, drob_2.numerator,
            drob_1.denominator, drob_2.denominator)
print('Произведение дробей (через Fraction) = ',
      float(Fraction(d_1)*Fraction(d_2)))
print("-------------------------------------------------")
sum_Drobi(drob_1.numerator, drob_2.numerator,
          drob_1.denominator, drob_2.denominator)
print('Сумма дробей (через Fraction) = ', float(Fraction(d_1)+Fraction(d_2)))
print("-------------------------------------------------")
