#!/usr/bin/python3
""" Python - Input/Output """


class Student:
    """ Class Student that defines a student by """

    def __init__(self, first_name, last_name, age):
        """ Class constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ that retrieves a dictionary representation
            of a Student instance """
        return self.__dict__
