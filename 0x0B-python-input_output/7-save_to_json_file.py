#!/usr/bin/python3
""" Python - Input/Output """
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file
        using a JSON representation """
    with open(filename, 'w', encoding='UTF8') as file:
        file.write(json.dumps(my_obj))
