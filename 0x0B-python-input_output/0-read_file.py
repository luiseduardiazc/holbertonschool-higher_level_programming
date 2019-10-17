#!/usr/bin/python3
""" Python - Input/Output """


def read_file(filename=""):
    """ Read file """
    with open(filename, 'r', encoding='UTF8') as file:
        for line in file:
            print(line)
