"""
Создайте программу выводящую информацию о системе вида:
Операционная система - ХХХ
Имя компьютера - ХХХ
Имя пользователя - ХХХ
"""

import os

print(f"os - {os.environ['OS']};\nPC_name - {os.environ.get('COMPUTERNAME')};\nuser_name - {os.environ['USERNAME']}")