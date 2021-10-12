#!/usr/bin/python3
"""This module has function that returns the list
of attributes and methods of an object."""


def lookup(obj):
    """This method returns the list of
    available attributes and methods of an object."""
    return dir(obj)
