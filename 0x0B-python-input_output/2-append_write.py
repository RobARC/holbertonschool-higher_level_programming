#!/usr/bin/python3
"""module append to a file"""


def append_write(filename="", text=""):
    """funtion to write a text in a file with append"""

    with open(filename, 'a', encoding='UTF-8') as f:
        return f.write(text)
