#!/usr/bin/python3
"""mudule square"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square inherit for class Rentangle """

    def __init__(self, size, x=0, y=0, id=None):
        """methode init to initialize instances of class Square"""

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ methode getter from size"""
        return self.__width

    @size.setter
    def size(self, value):
        """metodo setter from size"""
        self.width = value
        self.height = value

    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size> """

        cad = "[Square] ({}) {}/{} - {}"
        return cad.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Method Update """

        mylist = ['id', 'size', 'x', 'y']

        if args:
            for a, b in zip(mylist, args):
                # zip() It takes two or more sequences and creates
                # a new sequence of tuples    .
                # Each tuple contains one element from each list
                setattr(self, a, b)
        elif kwargs:
            for key, value in kwargs.items():
                if key in mylist:
                    setattr(self, key, value)

    def to_dictionary(self):
        "method dictionary"
        mydict = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }
        return mydict
