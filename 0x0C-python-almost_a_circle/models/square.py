#!/usr/bin/python3
"""This module defines a Square class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize an instance of a Square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the __str__ method to return a predefined string."""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """getter to obtain the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """setter to assign the width and the height(same value)."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
