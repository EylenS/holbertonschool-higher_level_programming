#!/usr/bin/python3
"""Defines a class called Square"""


class Square:
    """
    This class represents a square
    Attributes:
        size(int): size of the square - private attribute
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
