#!/usr/bin/python3
""" module my integer"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __init__(self, value):
        """Method to inicialize class MyInt"""

        super().__init__()

    def __eq__(self, other):
        """Method to inverted __eq__"""

        return super().__ne__(other)

    def __ne__(self, other):
        """Method to inverted __ne__"""

        return super().__eq__(other)
