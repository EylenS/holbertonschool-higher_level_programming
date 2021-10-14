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

    def to_json(self):
        """Retrieves a dictionary representation of
        a Student instance."""

        return self.__dict__
