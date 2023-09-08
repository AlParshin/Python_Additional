# Напишите программу, которая принимает две дроби с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.

# - doctest

import doctest


def multi_Drobi(a1, a2, b1, b2):
    """
    Даны две дроби.
    Проверим, что их произведение.
    :return: float
    >>> multi_Drobi(3, 5, 4, 8)
    0.46875
    >>> multi_Drobi(4, 6, 7, 9)
    0.38095238095238093
    >>> multi_Drobi(1, 2, 3, 6)
    0.1111111111111111
    """
    multi_chisliteley = a1 * a2
    multi_znamenateley = b1 * b2
    if b1 != b2:
        a1 = a1 * b2
        a2 = a2 * b1
        b1 = b1 * b2
    return multi_chisliteley/multi_znamenateley


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
    """
    Даны две дроби.
    Проверим, что их сумму.
    :return: float
    >>> sum_Drobi(3, 5, 4, 8)
    1.375
    >>> sum_Drobi(4, 6, 7, 9)
    1.2380952380952381
    >>> sum_Drobi(1, 2, 3, 6)
    0.6666666666666666
    """
    common_denominator = poisk_naimenshego_kratnogo(b1, b2)
    a1 *= common_denominator // b1
    b1 = common_denominator
    a2 *= common_denominator // b2
    b2 = common_denominator
    sum_chisliteley = a1 + a2
    divisor = sokrashenie_drobi(sum_chisliteley, common_denominator)
    sum_chisliteley //= divisor
    common_denominator //= divisor
    return sum_chisliteley / common_denominator


if __name__ == '__main__':
    doctest.testmod(verbose=10)
