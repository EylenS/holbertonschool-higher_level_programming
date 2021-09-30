#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle
        Arguments:
            width(int): width of the rectangle
            height(int): height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle
        Returns: width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets width
        Argument:
            value(int): width
        Raises:
            TypeError: the value of width is not an int
            ValueError: the value of width is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height
        Argument:
            value(int): height
        Raises:
            TypeError: the value of height is not an int
            ValueError: the value of height is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Print a rectangle
        Returns a rectangle shape in stdout."""
        aux = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                aux += str(self.print_symbol)
            if i != (self.__height - 1):
                aux += "\n"
        return aux

    def __repr__(self):
        """Return a string
        representation of the rectangle to be able to recreate
        a new instance."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message
        when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This method will not modify the state of the instance or the class
        returns the biggest rectangle based on the area
        Raises:
            TypeError: rect_1 and rect_2 must be an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Makes a new instance
        Arguments: --> size(int), which width == height == size
        Returns a square."""
        return Rectangle(size, size)
