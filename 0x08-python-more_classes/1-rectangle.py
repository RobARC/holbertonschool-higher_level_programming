#!/usr/bin/python3
"""This module create a Rectangle"""


class Rectangle:
    """This class define a Rectangle object"""
    def __init__(self, width=0, height=0):
        """Method init inicialize objects"""
        self.__height = height
        self.__width = width

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
