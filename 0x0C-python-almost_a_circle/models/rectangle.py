#!/usr/bin/python3
"""This module defines a Rectangle class."""


from models.base import Base


class Rectangle(Base):
    """This class defines a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance type Rectangle."""
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width."""
        self.__width = value

    @property
    def height(self):
        """getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height."""
        self.__height = value

    @property
    def x(self):
        """getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for s."""
        self.__x = value

    @property
    def y(self):
        """getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y."""
        self.__y = value
