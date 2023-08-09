def checkDate(date):
    mass = date.split(".")
    check = True
    # Общая проверка на валидность
    if (int(mass[0]) > 31) or (int(mass[0]) < 1):
        check = False
    elif (int(mass[1]) > 12) or (int(mass[1]) < 1):
        check = False
    elif (int(mass[2]) > 9999) or (int(mass[2]) < 1):
        check = False
    # Проверка на 30 дней в месяце
    for i in [4, 6, 9, 11]:
        if (int(mass[1]) == i) and (int(mass[0]) > 30):
            check = False
    return check


def checkForLeapYear(date):
    mass = date.split(".")
    check = True
    # Проверка на високосный год
    if (int(mass[1]) == 2):
        if int(mass[2]) % 4 == 0:
            if int(mass[0]) > 29:
                check = False
        else:
            if int(mass[0]) > 28:
                check = False
    return check
