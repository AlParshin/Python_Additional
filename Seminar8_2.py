# Напишите функцию, которая получает на вход директорию и рекурсивно обходит ее и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов сохраните его размер в байтах, а для директория - размер файлов в ней с учетом всех вложенных файлов и директорий.

import json
import os
import csv
import pickle
from pathlib import Path

BASE_DIR = 'D:/TEST/Python_Additional'
RES_JSON = 'res.json'
RES_CVS = 'res.cvs'
RES_PICKLE = 'res.pickle'
sub_dir_list = []
temp = os.listdir(BASE_DIR)
for el in temp:
    if os.path.isdir(os.path.join(BASE_DIR, el)):
        sub_dir_list.append(el)

for i in range(len(sub_dir_list)):
    dir_size = 0
    num_of_files_in_dir = 0
    for file in Path(os.path.join(BASE_DIR, sub_dir_list[i])).rglob('*'):
        if (os.path.isfile(file)):
            dir_size += os.path.getsize(file)
            num_of_files_in_dir += 1
    for full_path, dirs, files in os.walk(os.path.join(BASE_DIR, sub_dir_list[i])):
        el = files
    with open((os.path.join(BASE_DIR, RES_JSON)), "a") as f:
        json.dump({'name': sub_dir_list[i], 'full_path': full_path, 'size_in_byte': dir_size,
                  'number_of_files': num_of_files_in_dir, 'list_of_files': el}, f, indent=4)
    with open((os.path.join(BASE_DIR, RES_CVS)), "a", newline='') as c:
        csv_writer = csv.writer(c)
        csv_writer.writerow([{'name': sub_dir_list[i], 'full_path': full_path,
                            'size_in_byte': dir_size, 'number_of_files': num_of_files_in_dir, 'list_of_files': el}])
    with open((os.path.join(BASE_DIR, RES_PICKLE)), "ab") as p:
        pickle.dump({'name': sub_dir_list[i], 'full_path': full_path, 'size_in_byte': dir_size,
                    'number_of_files': num_of_files_in_dir, 'list_of_files': el}, p)
files_list = os.listdir(BASE_DIR)
for file in files_list:
    if os.path.isfile(os.path.join(BASE_DIR, file)):
        with open((os.path.join(BASE_DIR, RES_JSON)), "a") as f:
            json.dump({'name': str(file), 'full_path': BASE_DIR, 'size_in_byte': os.path.getsize(
                os.path.join(BASE_DIR, file)), 'isFile': True}, f, indent=4)
        with open((os.path.join(BASE_DIR, RES_CVS)), "a", newline='') as c:
            csv_writer = csv.writer(c)
            csv_writer.writerow([{'name': str(file), 'full_path': BASE_DIR, 'size_in_byte': os.path.getsize(
                os.path.join(BASE_DIR, file)), 'isFile': True}])
        with open((os.path.join(BASE_DIR, RES_PICKLE)), "ab") as p:
            pickle.dump({'name': str(file), 'full_path': BASE_DIR, 'size_in_byte': os.path.getsize(
                os.path.join(BASE_DIR, file)), 'isFile': True}, p)
