#!/usr/bin/python3
"""module retangle"""

from models.base import Base
 
class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ method init"""

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter width"""
        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
    @property
    def height(self):
        """getter  height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter height"""
        self.__height= height
        if type(height) is not int:
            raise TypeError("heigth mus be an integer")
        if height < 0:
            raise ValueError("heigth must be > 0")
    @property
    def x(self):
        """getter  x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        self.__x = x
        if x < 0:
            raise ValueError("x must be >= 0")
    @property
    def y(self):
        """getter  y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter y"""
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

        return "[Rentangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
    
        mylist = [id, width, heigth, 
        
        for self in args:
            self.__init__('args')
    
