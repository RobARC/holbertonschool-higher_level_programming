#!/usr/bin/python3
"""module class Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """Method init initialize objects"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = self.__dict__[i]
            except Exception as e:
                pass
        return new_dict

    def reload_from_json(self, json):
        """that replaces all attributes of the Student instance:
"""
        self.__dict__.update(json)
