#!/usr/bin/python3
""" Python - Input/Output """
import json


def class_to_json(obj):
    """ Function that returns the dictionary description
        with simple data structure """
    return obj.__dict__
