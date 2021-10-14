#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """This class defines a Student according to:
    first_name, last_name, age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student instances."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of
        a Student instance."""

        if type(attrs) is list:
            newDict = {}
            for attribute in attrs:
                if attribute in self.__dict__:
                    newDict[attribute] = self.__dict__[attribute]
            return newDict
        return self.__dict__
