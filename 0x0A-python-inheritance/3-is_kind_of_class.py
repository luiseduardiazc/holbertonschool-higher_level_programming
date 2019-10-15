#!/usr/bin/python3
"""
Python - Inheritance
"""


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of,
        or if the object is an instance of a class that inherited from
        the specified class otherwise False """
    try:
        is_instance = isinstance(obj, a_class)
    except Exception as inst:
        return False
    return is_instance
