# Даны стороны предполагаемого треугольника.
# Необходимо сообщить, существует ли вообще треугольник с такими сторонами.
# И дополнительно сообщить, является ли треугольник равнобедренным, равносторонним или все стороны разные.
# Реализуйте с помощью классов!

class Triangle:
    def __init__(self, storona_1: float, storona_2: float, storona_3: float) -> None:
        self.storona_1 = storona_1
        self.storona_2 = storona_2
        self.storona_3 = storona_3

    def print_triangle(self) -> None:
        print(
            f"Стороны = {self.storona_1}, {self.storona_2}, {self.storona_3}")

    def proverka(self) -> None:
        a = self.storona_1
        b = self.storona_2
        c = self.storona_3
        f = False
        if a + b <= c:
            print("Треугольника нет")
        elif a + c <= b:
            print("Треугольника нет")
        elif b + c <= a:
            print("Треугольника нет")
        else:
            print("Треугольник есть")
            f = True
        if f == True:
            if (a == b) and (c != a) and (c != b):
                print("Треугольник равнобедренный")
            elif (b == c) and (a != b) and (a != c):
                print("Треугольник равнобедренный")
            elif (a == c) and (b != a) and (b != c):
                print("Треугольник равнобедренный")
            elif (a == b == c):
                print("Треугольник равносторонний")
            else:
                print("Треугольник с разными сторонами")


print("-------------------------------------------------")
t1 = Triangle(1, 2, 3)
t1.print_triangle()
t1.proverka()
print("-------------------------------------------------")
t2 = Triangle(4, 5, 7)
t2.print_triangle()
t2.proverka()
print("-------------------------------------------------")
t3 = Triangle(4, 4, 4)
t3.print_triangle()
t3.proverka()
print("-------------------------------------------------")
t4 = Triangle(4, 4, 7)
t4.print_triangle()
t4.proverka()
print("-------------------------------------------------")
