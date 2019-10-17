#!/usr/bin/python3
""" Python - Input/Output """


def read_file(filename=""):
    """ Read file """
    with open(filename, encoding='utf-8') as file:
        file_read = file.read()
    print('{:s}'.format(read_file), end='')
