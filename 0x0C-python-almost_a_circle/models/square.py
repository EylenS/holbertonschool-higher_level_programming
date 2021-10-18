#!/usr/bin/python3
"""This module defines a Square class."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class """
    def __init__(self, size, x=0, y=0, id=None):
        """initialize an instance of a Square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the __str__ method to return a predefined string."""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
