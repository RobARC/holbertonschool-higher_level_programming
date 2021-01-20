#!/usr/bin/python3
""" Rectagle module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rentangle class"""

    def __init__(self, width, height):
        """Method init initialize objects"""
        self.__width = width
        self.__height = height
        self.integer_validator("with", width)
        self.integer_validator("height", height)
