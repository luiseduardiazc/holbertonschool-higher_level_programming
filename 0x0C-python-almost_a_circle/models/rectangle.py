#!/usr/bin/python3
""" module class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id=id)

    @property
    def width(self):
        """getter od width"""
        return self.__width

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return area calculation """
        return (self.width * self.height)

    def display(self):
        """ Prints in stdout the Rectangle
            instance with the character # """
        print("{}".format("\n" * self.y), end='')
        dis = "\n".join(" " * self.x + "#" *
                        self.width for x in range(self.height))
        print(dis)

    def __str__(self):
        """rectangule string representation"""
        rep = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return rep.format(self.id,
                          self.__x,
                          self.__y,
                          self.__width,
                          self.__height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        attr_list = [
            {'attr': 'id', 'exist': False},
            {'attr': 'width', 'exist': False},
            {'attr': 'height', 'exist': False},
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
        rec_dic["width"] = self.width
        rec_dic["height"] = self.height
        rec_dic["x"] = self.x
        rec_dic["y"] = self.y
        return rec_dic
