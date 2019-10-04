#!/usr/bin/python3
"""
int: Module 0. Integers addition


"""


def add_integer(a, b=98):
    """
    Write a function that adds 2 integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if type(a) or type(b) is float:
        a, b = int(a), int(b)
    return a + b
