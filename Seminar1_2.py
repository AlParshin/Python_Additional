print("Введите число от 0 до 99999:")
while True:
    a = int(input("a = "))
    if a >= 0 and a <= 99999:
        break
    else:
        print("Введите еще раз!")
if a == 0 or a == 1:
    print(f"Число {a} - исключение, оно ни простое, ни составное!")
else:
    f = True
    for i in range(2, a):
        if a % i == 0:
            f = False
            print(f"Число {a} - составное!")
            break
    if f == True:
        print(f"Число {a} - простое!")
