#!/usr/bin/python3
""" Python - Input/Output """


def read_lines(filename="", nb_lines=0):
    """ Function that reads n lines of a text file (UTF8)
        and prints it to stdout """
    num_lines = 0
    with open(filename, 'r', encoding='UTF8') as file:
        if nb_lines < 1:
            for line in file:
                print(line)
                num_lines += 1
        else:
            for x in range(nb_lines):
                print(file.readline())
                num_lines += 1
    return num_lines
