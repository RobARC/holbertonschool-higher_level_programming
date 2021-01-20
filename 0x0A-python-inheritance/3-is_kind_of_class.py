#!/usr/bin/python3
"""module contained the function """


def is_kind_of_class(obj, a_class):
    """ method is kind of class"""

    if isinstance(obj, a_class):
        return True
    if type(obj) == a_class:
        return True
    else:
        return False
