#!/usr/bin/python3
"""Defines a class called Square"""


class Square:

    """
    This class represents a square
    Attributes:
        size(int): size of the square - private attribute
    """

    def __init__(self, size):
        
        """Initializing the data
        Arguments:
            size: The size of a square
        """

        self.__size = size
