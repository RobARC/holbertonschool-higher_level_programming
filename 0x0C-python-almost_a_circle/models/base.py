#!/usr/bin/python3
""" module class base """
import json


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """method to initialize instances of class Base"""

        if id is not None:
                self.id = id
        else:
                Base.__nb_objects += 1
                self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method that returns Json string"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method Json string to a file"""

        filename = cls.__name__ + ".json"
        mylist = [""]

        if list_objs is None:
            with open(filename, 'w') as f:
                f.write(mylist)
        else:
            with open(filename, 'w') as f:

                for objects in list_objs:
                    mydic2 = cls.to_dictionary(objects)
                    mylist.append(mydic2)
                mydict = cls.to_json_string(mylist)
                f.write(mydict)

    @staticmethod
    def from_json_string(json_string):
        """method that returns the list of the JSON string"""

        if json_string is None or len(json_string) is 0:
            mylist = []
            return mylist
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates an object from a dictionary """
        dummy = cls(3, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        mylist = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                obj = cls.from_json_string(f.read())
                for mydicts in obj:
                    mylist.append(cls.create(**mydicts))
        except FileNotFoundError:
            return mylist
        return mylist
