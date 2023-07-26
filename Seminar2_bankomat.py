# Напишите программу "БАНКОМАТ":
# - Начальная сумма равна нулю
# - Допустимые действия: пополнить, снять, выйти
# - Сумма пополнения и снятия кратны 50 у.е.
# - Процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 у.е.
# - После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# - Нельзя снять больше, чем на счете
# - При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# - Любое действие выводит сумму денег

print("Введите начальный остаток на счете в у.е.:")
initial_balance = float(input())
count_popolnenie = 0
count_snyatie = 0
while True:
    # Если баланс > 5 млн, то минус 10% от баланса:
    if initial_balance > 5000000:
        print("Вы слишком богаты! Так нельзя! Мы вас раскулачим на 10%!")
        initial_balance = initial_balance - initial_balance*0.10
        print("Ваш баланс = ", round(initial_balance, 2))
    # Вводим тип операции: 1, 2 или 0:
    while True:
        print("Введите вид операции (1 - пополнение, 2 - снятие, 0 - выход):")
        operation_type = int(input())
        if operation_type in [1, 2, 0]:
            break
        else:
            print("Введено некорректное значение! Повторите ввод!")
    # Операция пополнения счета
    if operation_type == 1:
        while True:
            print("Введите сумму, на которую пополнить счет, кратную 50:")
            sum_popolnenie = float(input())
            if (sum_popolnenie % 50 == 0):
                break
            else:
                print("Введено некорректное значение! Повторите ввод!")
        count_popolnenie += 1
        if count_popolnenie % 3 == 0:
            print("Вы сделали три операции! Это мощно! Вам кэшбек за это +3% на баланс!")
            initial_balance = (initial_balance + sum_popolnenie)*1.03
        else:
            initial_balance = initial_balance + sum_popolnenie
        print("Ваш баланс = ", round(initial_balance, 2))
        print("Количество исполненных операций пополнения счета = ", count_popolnenie)
    # Операция снятия денежных средств
    if operation_type == 2:
        while True:
            print("Введите сумму снятия средств, кратную 50:")
            sum_snyatie = float(input())
            if (sum_snyatie % 50 == 0) and (sum_snyatie < initial_balance):
                break
            else:
                print("Введено некорректное значение! Повторите ввод!")
        # Расчет комиссии за операцию
        if sum_snyatie * 0.05 < 30:
            komissiya = 30
        elif sum_snyatie * 0.05 > 600:
            komissiya = 600
        else:
            komissiya = sum_snyatie * 0.05
        print("Комиссия за операцию = ", round(komissiya, 2))
        count_snyatie += 1
        if count_snyatie % 3 == 0:
            print("Вы сделали три операции! Это мощно! Вам кэшбек за это +3% на баланс!")
            initial_balance = (initial_balance - sum_snyatie - komissiya)*1.03
        else:
            initial_balance = initial_balance - sum_snyatie - komissiya
        print("Ваш баланс = ", round(initial_balance, 2))
        print("Количество исполненных операций пополнения счета = ", count_snyatie)
    # Выход
    if operation_type == 0:
        break
print("Спасибо, что воспользовались нашими услугами! До новых встреч!")
print("Ваш итоговый баланс = ", round(initial_balance, 2))
