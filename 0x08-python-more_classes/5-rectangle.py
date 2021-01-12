#!/usr/bin/python3
"""This module create a Rectangle"""


class Rectangle:
    """This class define a Rectangle object"""
    def __init__(self, width=0, height=0):
        """Method init initialize objects"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """getter method, return private height"""
        return self.__height

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
        return self.__width

    @width.setter
    def width(self, value):
        """with setter, sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Return rectangle area"""
        area = self.width * self.height
        return area

    def perimeter(self):
        """Return rectangle perimeter"""
        perimeter = 2 * (self.width + self.height)
        if self.width == 0 or self.height == 0:
            perimeter = 0
        return perimeter

    def __str__(self):
        """:return rectagle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        c = "#" * self.__width + '\n'
        return (c * self.__height)[:-1]

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
