#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """Makes a BaseGeometry class."""

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
