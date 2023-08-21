# Создать декоратор для использования кэша.
# Т.е. сохранять аргументы и результаты в словарь, если вызывается функция с аргументами,
# которые уже записаны в кэше - вернуть результат из кэша, если нет - выполнить функцию.
# Кэш лучше хранить в json.
# Решение, близкое к решению данной задачи было разобрано на семинаре.

from typing import Callable

import json


def json_logging(func: Callable):
    try:
        with open(f'{func.__name__}.json', 'r') as data:
            result_list = json.load(data)
    except FileNotFoundError:
        result_list = []

    def wrapper(*args, **kwargs):
        result = func(args, kwargs)
        keys = list(kwargs.keys())
        # open(f'(func.__name__).json', 'a')
        with open(f'(func.__name__).json', 'r') as data:
            s = data.read().replace('[', '').replace(
                ']', '').replace(' ', '').replace('\n', '')
            s = s.replace('}{', '},{')
            kortezh = eval(s)
            f = True
            for el in kortezh:
                if (el['keys'] == str(kwargs.get(keys[0]))+str(kwargs.get(keys[1]))) or (el['keys'] == str(kwargs.get(keys[1]))+str(kwargs.get(keys[0]))):
                    print("Такое значение уже есть и равно = ", el['sum'])
                    print("В файл не будет ничего добавлено!")
                    f = False
                    break
            if f == True:
                result_list.append({'keys': str(kwargs.get(keys[0])) + ' ' + str(
                    kwargs.get(keys[1])), 'sum': kwargs.get(keys[0])+kwargs.get(keys[1])})
        with open(f'(func.__name__).json', 'a') as data:
            json.dump(result_list, data, indent=4)
        return result
    return wrapper


@json_logging
def guessing(a, b):
    1


guessing(a=int(input()), b=int(input()))
