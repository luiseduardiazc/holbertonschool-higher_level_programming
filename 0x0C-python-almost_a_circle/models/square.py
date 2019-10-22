#!/usr/bin/python3
""" module class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ construnctor """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """ Square string representation"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Method that assigns attributes """
        attr_list = [
            {'attr': 'id', 'exist': False},
            {'attr': 'size', 'exist': False},
            {'attr': 'x', 'exist': False},
            {'attr': 'y', 'exist': False}
        ]
        for key, value in enumerate(args):
            attr = attr_list[key]['attr']
            attr_list[key]['exist'] = True
            self.__setattr__(attr, value)
        for key, value in kwargs.items():
            for k in range(len(attr_list)):
                attr = attr_list[k]['attr']
                exist = attr_list[k]['exist']
                if (attr == key) and not exist:
                    self.__setattr__(key, value)

    def to_dictionary(self):
        """dictionary representation"""
        rec_dic = {}
        rec_dic["id"] = self.id
        rec_dic["size"] = self.size
        rec_dic["x"] = self.x
        rec_dic["y"] = self.y
        return rec_dic
