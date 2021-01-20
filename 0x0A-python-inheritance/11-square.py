#!/usr/bin/python3
""" Square module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size):
        """Method init initialize objects"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """method return square area"""
        area = super().area()
        return area

    def __str__(self):
        """should return [Rectangle] <width>/<height>"""

        return "[Square] {}/{}".format(self.__size, self.__size)
