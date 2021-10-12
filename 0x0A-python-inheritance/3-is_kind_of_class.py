#!/usr/bin/python3
"""Defines a function that evaluates
if the object is from the same class or inherit."""


def is_kind_of_class(obj, a_class):
    """This function evaluates if the object is from the same
    class or inherit.
    Returns:
        True if the object is an instance of, or if the object
            is an instance of a class that inherited from,
            the specified class.
        False: otherwise."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
