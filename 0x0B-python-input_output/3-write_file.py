#!/usr/bin/python3
""" Python - Input/Output """


def write_file(filename="", text=""):
    """ Function that reads n lines of a
        text file (UTF8) and prints it to stdout """
    with open(filename, 'w', encoding='UTF8') as file:
        return file.write(text)
