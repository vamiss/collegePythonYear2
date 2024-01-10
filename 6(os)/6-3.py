"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""

import os

path = os.getcwd()

for i in range(11):
    try:
        if i in [2, 4, 6, 8, 10]:
            os.rename(rf"{path}\target\{i}", rf"{path}\target\kaplanNumber{i}")
    except:
        print("File is already renamed or doesn't exist")