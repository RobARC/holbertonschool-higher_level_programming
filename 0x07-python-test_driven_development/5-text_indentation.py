#!/bin/usr/python3
"""module text_identation"""


def text_indentation(text):
    """function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """

    a = '.'
    b = 0
    c = '?'
    d = ':'

    if type(text) != str:
        raise TypeError("text must be a string")

    lenght = len(text)
    while b < lenght:
        print(text[b], end="")
        if text[b] is a or text[b] is c or text[b] is d:
            print("\n")
            if (b + 1) < lenght:
                while text[b + 1] is " ":
                    b += 1
        b += 1
