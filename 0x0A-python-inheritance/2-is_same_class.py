#!/usr/bin/python3
"""Defines a function
that evaluates if it is an instance of the class."""


def is_same_class(obj, a_class):
    """This function function evaluates if tje object
    is an instance of the a_class class.
    Returns:
        True: if the object is exactly an instance
        False: otherwise."""
    if type(obj) == a_class:
        return True
