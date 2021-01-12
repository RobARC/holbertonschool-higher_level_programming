#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        self.__class__.number_of_instances += 1

    def area(self):
        area = self.__width * self.__height
        return area

    def perimeter(self):
        perimeter = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        return perimeter

    def __str__(self):
        """:return rectagle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        c = str(self.print_symbol) * self.__width + '\n'
        return (c * self.__height)[:-1]

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

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
