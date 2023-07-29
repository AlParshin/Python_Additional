# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# Например [1,2,3,1,2,4,5] --> [1,2]

start = [1, 3, 4, 7, 8, 4, 5, 6, 7, 3, 2, 9, 0, 4, 2, 1, 2, 3, 7, 0]
temp = []
dict_count = {}
final = []

# Сложный способ решения:
for el in start:
    dict_count[el] = 0
    if el not in temp:
        temp.append(el)
for el in start:
    if el in temp:
        dict_count[el] += 1
for el in dict_count:
    if dict_count[el] > 1:
        final.append(el)
print(sorted(final))

# Легкий способ:
finish = dict((x, start.count(x)) for x in set(start) if start.count(x) > 1)
print(list(finish))
