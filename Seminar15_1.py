# Треугольник

import logging

print("Длины сторон треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

logging.basicConfig(level=logging.INFO, filename="Task_1.log", filemode="a",
                    encoding="UTF-8", format="%(asctime)s %(levelname)s %(message)s")

logging.info(f"Значения сторон треугольника: {a}, {b} and {c}.")

f = True

if a + b <= c:
    logging.error("Треугольника нет\n---")
    f = False
elif a + c <= b:
    logging.error("Треугольника нет\n---")
    f = False
elif b + c <= a:
    logging.error("Треугольника нет\n---")
    f = False
else:
    logging.info("Треугольник есть")

if (a == b) and (c != a) and (c != b):
    logging.info("Треугольник равнобедренный\n---")
elif (b == c) and (a != b) and (a != c):
    logging.info("Треугольник равнобедренный\n---")
elif (a == c) and (b != a) and (b != c):
    logging.info("Треугольник равнобедренный\n---")
elif (a == b == c):
    logging.info("Треугольник равносторонний\n---")
else:
    if f == True:
        logging.info("Треугольник с разными сторонами\n---")
