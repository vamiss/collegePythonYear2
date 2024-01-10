""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""

import os

path = os.getcwd()

os.mkdir(rf"{path}\task4")

os.chdir(rf"{path}\task4")

with open("answer.txt", "w+") as newfile:
    newfile.write("Task is completed")