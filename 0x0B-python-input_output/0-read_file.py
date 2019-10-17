#!/usr/bin/python3
""" Python - Input/Output """


def read_file(filename=""):
    """ Read file """
    with open(filename, 'r', encoding='utf-8') as file:
        file_read = file.read()
    print('{}'.format(read_file), end='')
