#!/usr/bin/python3
"""Module Add Attibute"""


def add_attribute(obj, attribute, value):
    """function Add an attribute to an object if it's possible"""

    if '__dic__' in dir(obj):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
