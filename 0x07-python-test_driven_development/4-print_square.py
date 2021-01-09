#!/usr/bin/python3
""" Square module print square """


def print_square(size):
    """print square to stdout with character #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        c = "#"
        for j in range(size):
            print(c * size)
