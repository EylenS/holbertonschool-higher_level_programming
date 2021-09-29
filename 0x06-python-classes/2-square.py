#!/usr/bin/python3
"""Defines a class called Square"""


class Square:

    """
    This class represents a square
    Attributes:
        size(int): size of the square - private attribute
    """

    def __init__(self, size=0):

        """Instantiation with size
        Argument:
            __size: is private attribute
        Raises:
            TypeError: The value of size gotten is not am int
            ValueError:The value gottenis less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
