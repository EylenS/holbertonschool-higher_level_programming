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

    def update(self, *args, **kwargs):
        """This method updates attrs by:
        *args: takes arguments as a tuple.
        **kwargs: takes arguments as a dict.
        The parameters are associated according to the dict keys.."""
        # using len() method in args to count
        if len(args) >= 1:
            # enumerate() method adds counter to an iterable and returns it
            for idx, item in enumerate(args):
                if idx == 0:
                    self.id = item
                elif idx == 1:
                    self.size = item
                elif idx == 2:
                    self.x = item
                elif idx == 3:
                    self.y = item
        else:
            for key in kwargs.keys():
                if key == "id":
                    self.id = kwargs["id"]
                if key == "size":
                    self.size = kwargs["size"]
                if key == "x":
                    self.x = kwargs["x"]
                if key == "y":
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """This method returns the dict representation of a Square."""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
