#!/usr/bin/python3
""" Square module """


class Square:
    """Square class"""

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        """Size getter, return the private size"""

        return(self.__size)

    @size.setter
    def size(self, value):
        """Size setter, sets the size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print square to stdout with character #"""
        c = "#"
        for j in range(self.__size):
            print(c * self.__size)
