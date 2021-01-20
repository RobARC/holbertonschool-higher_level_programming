#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """BaseGeometry Class"""

    def area(self):
        """ method area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method integer_validator """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
