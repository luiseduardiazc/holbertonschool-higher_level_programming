#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) and type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] and value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        coordinate_x = self.position[0]
        coordinate_y = self.position[1]
        # print \n in y
        if coordinate_y > 0 and self.size != 0:
            for y in range(0, coordinate_y):
                print()
        for row in range(self.size):
            for x in range(coordinate_x):
                # print spaces in x
                print(" ", end='')
            for colum in range(self.size):
                print("#", end='')
            print()
        if self.size == 0:
            print()
