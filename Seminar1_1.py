print("Длины сторон треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b <= c:
    print("Треугольника нет")
elif a + c <= b:
    print("Треугольника нет")
elif b + c <= a:
    print("Треугольника нет")
else:
    print("Треугольник есть")

if ((a == b) and (c != a) and (c != b)) or ((b == c) and (a != b) and (a != c)) or ((a == c) and (b != a) and (b != c)):
    print("Треугольник равнобедренный")
elif (a == b == c):
    print("Треугольник равносторонний")
else:
    print("Треугольник разносторонний")
