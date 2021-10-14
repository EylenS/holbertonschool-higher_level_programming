#!/usr/bin/python3
"""This module contains a function that returns
the dictionary for JSON serialization of an object."""


def class_to_json(obj):
    """This fun returns the dictionary with simple data structure
    for JSON serialization of an object.
        -> obj is an instance of a Class
        -> All attributes of the obj Class are serializable: list,
        dictionary, string, integer and boolean."""
    return obj.__dict__
