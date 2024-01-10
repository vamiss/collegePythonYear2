"""
Из файла Task1.csv выведите данные в формате:
Имя - Звание
"""

import csv

with open('3-1.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for i in reader:
        print(f'{i[0]} - {i[3]}')