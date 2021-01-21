#!/usr/bin/python3
"""Module function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:"""


def class_to_json(obj):
    """function that return a object python in a JSON"""

    objclass = obj

    return objclass.__dict__
