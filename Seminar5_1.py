# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трех элементов: путь, имя файла, расширение файла.
# Ввод: "C:/Users/Vladislav/Desktop/deep_to_python/test.txt"
# Вывод: "C:/Users/Vladislav/Desktop/deep_to_python", "test", "txt"

enter = "C:/Users/Vladislav/Desktop/deep_to_python/test.txt"
exit = []
string = ''
*head, tail = enter.split("/")
for el in head:
    string += el
    string += '/'
exit.append(string)
for el in tail.split("."):
    exit.append(el)
print(exit)
