#!/usr/bin/python3
"""module write file"""


def write_file(filename="", text=""):
    """funtion to write a text in a file"""

    with open(filename, 'w', encoding='UTF-8') as f:
        return f.write(text)
