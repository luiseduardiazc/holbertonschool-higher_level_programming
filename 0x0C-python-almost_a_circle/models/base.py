#!/usr/bin/python3
""" module class Base """


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor: if id is not None,
            assign the public instance attribute
            id with this argument value """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
