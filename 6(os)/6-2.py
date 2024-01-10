"""
Создайте программу создающую папку target внутри которой еще 10 папок имена которых цифры от 1 до 10
"""

import os

try:
    os.mkdir(r"C:\Users\Vamiss8\PycharmProjects\lalala\6(os)\target")
except:
    print('Directory named "target" is already exist')

try:
    for i in range(10):
        os.mkdir(rf"C:\Users\Vamiss8\PycharmProjects\lalala\6(os)\target\{i+1}")
except:
    print('Files named "1-10" are already exist')