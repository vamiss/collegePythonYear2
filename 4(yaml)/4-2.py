"""
Из файла info.yaml выведите имя и id Ливерпуля
"""

import yaml
from pprint import pprint

with open('info.yaml') as yaml_file:
    reader = yaml.safe_load(yaml_file)
    pprint(f'name = {reader[0]["name"]}; id = {reader[0]["id"]}')
 