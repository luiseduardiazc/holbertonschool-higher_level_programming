#!/usr/bin/python3
"""Empty class Rectangle that defines a rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        result = ""
        if self.perimeter() == 0:
            return result
        for index in range(self.__height):
            result += str("#" * self.__width)
            if index < self.__height - 1:
                result += "\n"
        return result

    def __repr__(self):
        result = "Rectangle({}, {})"
        return result.format(eval(str(self.__width)), eval(str(self.__height)))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
