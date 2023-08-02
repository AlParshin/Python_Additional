# Создайте функцию генератор чисел Фибоначчи

def fibonacci(n):
    print(f"Первые {n} из чисел Фибоначчи (число 0 не учитываем):")
    a1 = 0
    a2 = 1
    i = 0
    while i < n:
        temp = a1 + a2
        a1 = a2
        a2 = temp
        print(temp)
        i += 1


print("Введите количество чисел Фибоначчи, которые хотите вывести на экран:")
kolvo = int(input())
fibonacci(kolvo)
