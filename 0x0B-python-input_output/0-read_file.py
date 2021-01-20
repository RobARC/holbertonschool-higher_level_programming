#!/usr/bin/python3
"""module read a text file"""


def read_file(filename=""):
    """function to read a text file"""

    with open(filename, 'r') as f:
        print(f.read(), end="")
