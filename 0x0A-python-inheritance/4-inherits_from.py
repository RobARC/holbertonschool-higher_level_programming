#!/usr/bin/python3
""" module that contained function inherits_from """


def inherits_from(obj, a_class):
    """ function that returns True if the object is an
    instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
     """
    b = type(obj)
    if (b is a_class):
        return False
    if issubclass(b, a_class):
        return True
    else:
        return False
