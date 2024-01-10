"""
Запишите словарь в yaml файл
"""
to_yaml = {
   'access': ['switchport mode access',
              'switchport access vlan',
              'switchport nonegotiate',
              'spanning-tree portfast',
              'spanning-tree bpduguard enable'],
   'trunk': ['switchport trunk encapsulation dot1q',
             'switchport mode trunk',
             'switchport trunk native vlan 999',
             'switchport trunk allowed vlan'],
}

import yaml

with open('kaplan.yaml', 'w') as yaml_file:
    yaml.dump(to_yaml, yaml_file)