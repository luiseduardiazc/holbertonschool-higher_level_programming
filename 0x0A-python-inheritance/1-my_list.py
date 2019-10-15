#!/usr/bin/python3
"""
Python - Inheritance
"""


class MyList(list):
    """ class MyList that inherits from list """

    def print_sorted(self):
        """ prints the list, sorted (ascending sort) """
        print(sorted(self))
