#!/usr/bin/python3
""" module class Base """
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ eturns the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file_name = str(cls.__name__) + ".json"
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())

        with open(file_name, 'w') as writer:
            writer.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create new instance and update """
        dummy = object
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        file_name = cls.__name__ + ".json"
        list_line_file = []
        list_instances = []
        if not os.path.isfile(file_name):
            return list_file
        with open(file_name, 'r') as reader:
            for line in reader:
                list_line_file.append(cls.from_json_string(line))
        for items in list_line_file:
            for dic_to_update in items:
                obj = cls(1, 1)
                obj.update(**dic_to_update)
                list_instances.append(obj)
        return list_instances
