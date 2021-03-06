#!/usr/bin/python3
""" Module to add two integer """


def add_integer(a, b=98):
    """ funtion to add two integer
        Args: a: int b: int
        Returns: sum of a and b
    """

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return (a + b)
