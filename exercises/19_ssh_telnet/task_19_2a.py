# -*- coding: utf-8 -*-
'''
Задание 19.2a

Скопировать функцию send_config_commands из задания 19.2 и добавить параметр verbose,
который контролирует будет ли выводится на стандартный поток вывода
информация о том к какому устройству выполняется подключение.

По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, verbose=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства из файла devices.yaml с помощью функции send_config_commands.
'''
import netmiko
import yaml

commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]

def send_show_command(device,commands,verbose=True):
    if verbose:
        print(f'Connect to {device["ip"]}...')
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(commands)

    return result

with open('devices.yaml') as f:
    devices = yaml.safe_load(f)
    for device in devices:
        print(send_show_command(device,commands))
        print('-'*20)




