#!/usr/bin/python3
"""module retangle that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ method init class constructor"""

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """method privated getter width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Method privated setter width of Rectangle"""
        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """Method Privated getter  height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """Method Privated setter height of Rectagle"""
        self.__height = height
        if type(height) is not int:
            raise TypeError("heigtht mus be an integer")
        if height < 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """Metod Privated getter  x of Rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        """Method privated setter x of Rectangle"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        self.__x = x
        if x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """Method Privated getter  y of Rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        """Method privated setter y of Rectangle"""
        self.__y = y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """ Return the area of the rectangle"""
        return self.width * self.height

    def display(self):

            for b in range(self.y):
                print()

            c = '#'
            for a in range(self.height):
                print(" " * self.x, end="")
                print(c * self.width)

    def __str__(self):
        """[Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        mystr = "[Rectangle] ({}) {}/{} - {}/{}"
        return mystr.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Metho update class Rectangle by overring 
        __str__ method tha return
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        mylist = ['id', 'width', 'height', 'x', 'y']
        if args:
            for a, b in zip(mylist, args):
                #zip() It takes two or more sequences and creates
                #a new sequence of tuples Each tuple contains one
                #element from each list
                setattr(self, a, b)
        elif kwargs:
            for key, value in kwargs.items():
                if key in mylist:
                    setattr(self, key, value)

    def to_dictionary(self):
        """method dictionary return the dictionary
        of a Rectangle
        """
        mydict = {'id': self.id, 'width': self.width, 'height': self.height,
                  'x': self.x, 'y': self.y}
        return mydict
