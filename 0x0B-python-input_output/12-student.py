#!/usr/bin/python3
""" Python - Input/Output """
import json


class Student:
    """ Class Student that defines a student by """

    def __init__(self, first_name, last_name, age):
        """ Class constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ that retrieves a dictionary representation
            of a Student instance """
        dict_rep = self.__dict__
        dict_filtered = {}
        is_list_string = True
        if isinstance(attrs, list):
            for item in attrs:
                if type(item) is not str:
                    is_list_string = False
                    break
                elif dict_rep.get(item, False):
                    dict_filtered[item] = dict_rep[item]
        else:
            is_list_string = False

        if is_list_string and dict_filtered:
            return dict_filtered
        return dict_rep
