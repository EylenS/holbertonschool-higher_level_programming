#!/usr/bin/python3
"""Defines an addition operation between two integers."""


def add_integer(a, b=98):
    """Addition operation,
    Arguments:
        a and b are integers, if they're float the could be converted into int.
    Returns:
        The result of the sum.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(a) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
