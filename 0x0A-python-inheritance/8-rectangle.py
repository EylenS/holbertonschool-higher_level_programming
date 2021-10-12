#!/usr/bin/python3
"""Defines a geometry op."""


class BaseGeometry:
    """Makes a BaseGeometry class."""
    pass

    def area(self):
        """This method hasn't been implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This module validates the value.
        name: type string.
        value: type int."""
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry class."""

    def __init__(self, width, height):
        """Initializes an instance withe its attributes:
        width and height must be positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
