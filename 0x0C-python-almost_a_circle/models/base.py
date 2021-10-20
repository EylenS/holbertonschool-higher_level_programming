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
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """This method writes the JSON string representation of
        list_objs to a file.
        list_objs: list of instances who inheritances from Base."""
        listObjs = []
        if list_objs is None:
            listObjs = []
        else:
            for obj in list_objs:
                listObjs.append(obj.to_dictionary())
        jsonStr = Base.to_json_string(listObjs)
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(jsonStr)

    @staticmethod
    def from_json_string(json_string):
        """This method returns the list of the JSON string representation
        json_string. -> json_string is a str representing a list of dicts."""
        if json_string is None or len(json_string) == 0:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """This method returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 2)
            dummy.update(**dictionary)
        elif cls.__name__ == "Square":
            dummy = cls(5)
            dummy.update(**dictionary)
        return dummy
