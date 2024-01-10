"""
Из данных в файле Task1.csv сделайте словарь вида:
(Имя,фамилия):{оценка: звание}
"""

import csv
dict = {}

with open('3-1.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for i in reader:
        dict[(i[0], i[1])] = {i[2] : i[3]}
    print(dict)