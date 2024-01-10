"""
Создайте список предметов формата Название, препод, ваша любовь к предмету(от 0 до 10).
Сохраните в CSV файл(название файла - ваша фамилия).
P.S не менее 4 столбцов.
"""

dict_to_scv = [['vved', 'golovin', 8],
               ['oss', 'mihailov', 8],
               ['proga', 'babchenok', 10],
               ['algo', 'vakansiya', 4]]

import csv

with open('kalan.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for i in dict_to_scv:
        writer.writerow(i)