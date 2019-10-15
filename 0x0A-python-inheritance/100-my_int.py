#!/usr/bin/python3
"""
Python - Inheritance
"""


class MyInt(int):
    """ class MyInt that inherits from int """

    def __init__(self, value):
        self.__value = value

    def __eq__(self, obj):
        """ operator == inverted """
        return self.__value != obj

    def __ne__(self, obj):
        """ operator != inverted """
        return self.__value == obj
