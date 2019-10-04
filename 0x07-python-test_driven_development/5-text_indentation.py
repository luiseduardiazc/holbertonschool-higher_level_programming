#!/usr/bin/python3
"""
int: Module 0. Integers addition


"""


def text_indentation(text):
    """
    unction that prints a text with 2 new lines after each of
    these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for chr in text:
        if chr in ('.', '?', ':'):
            print("{}".format(chr), end='\n\n')
        else:
            print("{}".format(chr), end='')
    print("\n")
