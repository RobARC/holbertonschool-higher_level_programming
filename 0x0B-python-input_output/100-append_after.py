#!/usr/bin/python3
"""module that insert a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """module that insert a line of text to a file"""

    text = ""
    with open(filename, mode='r+', encoding='utf-8') as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, 'w') as f:
        f.write(text)
