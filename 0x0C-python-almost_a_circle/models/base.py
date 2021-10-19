#!/usr/bin/python3
"""This module defines a base class."""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method returns the JSON string representation
        of list_dictionaries."""
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return []
        return (json.dumps(list_dictionaries))
