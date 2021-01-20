#!/usr/bin/python3
"""Modulo class MyList"""


class MyList(list):
    """ class MyList"""

    def print_sorted(self):
        """ method print sorted list"""

        print(sorted(self))
