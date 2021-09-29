#!/usr/bin/python3
"""Defines a class called Square"""


class Square:

    """
    This class represents a square
    Attributes:
        size(int): size of the square - private attribute
    """

    def __init__(self, size=0):

        """Initializes the data: size
        Argument:
            size: size of a square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size
        Arguments:
            value(int): value to assign size
        Raises:
            TypeError: The value of size gotten is not am int
            ValueError:The value gottenis less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        """Calculates the area of square
        and returns an actual squar area
        """
        a = self.__size**2
        return a

    def my_print(self):
        """ Prints in stdout the square with the character #"""
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
        elif self.__size == 0:
            print("")
