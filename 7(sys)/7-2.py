"""
Напишите скрипт который получает системный ввод от пользователя и выводит надпись "команда принята" если ввод начинается
с sys.in.
"""
import sys
a = input('')
if a.startswith('sys.in'):
    print('Command is accepted.')