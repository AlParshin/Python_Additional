# Напишите функцию, принимающую на вход только ключевые параметры(kwargs) и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хэшируем, используйте его строковое представление.
# Пример:
# reverse_kwargs(rev=True, acc="YES", stroka=4) --> {True:"rev", "YES":'acc', 4:"stroka"}

def slovar(**kwargs):
    dict = {}
    for first, second in kwargs.items():
        dict[second] = first
    return dict


print(slovar(rev=True, acc="YES", stroka=4))
