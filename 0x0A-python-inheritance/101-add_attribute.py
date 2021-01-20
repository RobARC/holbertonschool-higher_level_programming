#!/usr/bin/python3
"""Module Add Attibute"""


def add_attribute(obj, attribute, value):
    """function Add an attribute to an object if it's possible"""

    if hasattr(obj, '__dict__') is not True:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
