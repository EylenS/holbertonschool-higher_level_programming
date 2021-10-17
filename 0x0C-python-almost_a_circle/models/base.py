#!/usr/bin/python3
"""This module defines a base class."""


class Base:
    """Defines a Base class.
    __nb_objects is a private class attribute."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor. Initialize an instance.
        Args -> id(int)."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
