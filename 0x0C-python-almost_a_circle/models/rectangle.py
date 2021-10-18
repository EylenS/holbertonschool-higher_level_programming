#!/usr/bin/python3
"""This module defines a Rectangle class."""


from models.base import Base


class Rectangle(Base):
    """This class defines a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance type Rectangle. Defines the parameters.
        and attributes are declared."""
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

# The methods to obtain the private attributes are defined by getter.
# To modify them: setter

    @property
    def width(self):
        """getter to obtain width."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter to modify width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter to obtain height."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter to modify height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter to obtain x."""
        return self.__x

    @x.setter
    def x(self, value):
        """setter to modify x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter to obtain y."""
        return self.__y

    @y.setter
    def y(self, value):
        """setter to modify y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This method returns the Rectangle's area."""
        return self.__width * self.__height

    def display(self):
        """This method prints in stdout the shape of the
        Rectangle instance with the character #."""
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Overrides the __str__ method to return a predefined string."""
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args):
        """This method assigns an argument to each attribute."""
        if len(args) >= 1:
            # enumerate() method adds counter to an iterable and returns it.
            # The returned object is an enumerate object.
            for idx, item in enumerate(args):
                if idx == 0:
                    self.id = item
                elif idx == 1:
                    self.width = item
                elif idx == 2:
                    self.height = item
                elif idx == 3:
                    self.x = item
                elif idx == 4:
                    self.y = item
