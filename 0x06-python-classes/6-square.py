#!/usr/bin/python3
""" Square module """


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        """Size getter, return the private size"""

        return(self.__size)

    @size.setter
    def size(self, value):
        """Size setter, sets the size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position square"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type((position[0]) != int or type(position[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """print square to stdout with character #"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            c = "#"
            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print(c * self.__size)
