#!/usr/bin/python3
"""This module create a Rectangle"""


class Rectangle:
    """This class define a Rectangle object"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method init initialize objects"""
        self.height = height
        self.width = width
        self.__class__.number_of_instances += 1

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
        c = str(self.print_symbol) * self.__width + '\n'
        return (c * self.__height)[:-1]

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Method that returns a new Rectangle
        instance with width == height == size
        """
        return cls(size, size)
