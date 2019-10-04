#!/usr/bin/python3
"""
int: Module 0. Integers addition


"""


def print_square(size):
    """
      function that prints a square with the character #
    """
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for row in range(size):
        print("{}".format("#" * size), end='\n')
