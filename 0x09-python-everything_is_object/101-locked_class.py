#!/usr/bin/python3
"""Module that defines a locked class"""


class LockedClass:
    """that prevents the user from dynamically c
    reating new instance attributes, except if the
    new instance attribute is called first_name."""

    __slots__ = ['first_name']
