#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    def area(self):
        area = self.__width * self.__height
        return area

    def perimeter(self):
        perimeter = 2 * (self.__width + self.__height)
        return perimeter

    @property
    def height(self):
        """getter method, return private height"""

        return (self.height)

    @height.setter
    def height(self, value):
        """height.setter, sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """getter method, return private width"""

        return (self.width)

    @width.setter
    def width(self, value):
        """with setter, sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
