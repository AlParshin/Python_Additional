# Напишите функцию, которая сериализует содержимое текущей директории в json-файл.
# В файле должен храниться список словарей, словарь описывает элемент внутри директории имя, расширение, тип.
# Если элемент - директория, то только тип и имя.
# Пример результата для папки, где лежит файл test.txt и директория directory_test
# [
# {
# 'name' 'test',
# 'extension' 'txt',
# 'type' 'file'
# },
# {
# 'name' 'directory_test',
# 'type' 'directory',
# }
# ]

import json
import os

PATH = 'D:/TEST/Python_Additional'
RES_JSON = 'res.json'

files_list = os.listdir(PATH)
for file in files_list:
    if os.path.isfile(os.path.join(PATH, file)):
        name, extension = file.split(".")
        with open((os.path.join(PATH, RES_JSON)), "a") as f:
            json.dump({'name': name, 'extension': extension,
                      'type': 'file'}, f, indent=4)
    elif os.path.isdir(os.path.join(PATH, file)):
        with open((os.path.join(PATH, RES_JSON)), "a") as f:
            json.dump({'name': file, 'type': 'directory'}, f, indent=4)
with open((os.path.join(PATH, RES_JSON)), "a") as f:
    name, extension = RES_JSON.split(".")
    json.dump({'name': name, 'extension': extension,
              'type': 'file'}, f, indent=4)
f.close()
