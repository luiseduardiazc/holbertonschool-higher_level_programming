#!/usr/bin/python3
""" Python - Input/Output """


def number_of_lines(filename=""):
    """ Read number lines """
    number_of_lines = 0
    with open(filename, 'r', encoding='UTF8') as file:
        for line in file:
            number_of_lines += 1
    return number_of_lines
