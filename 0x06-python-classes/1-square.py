#!/usr/bin/python3
"""Defines a class called Square"""


class Square:
    """Square represents a square

    Attributes:
        _size(int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes a square

        Args:
            size(int)size of a side of the square

        Returns: None
        """
        self._size = size
