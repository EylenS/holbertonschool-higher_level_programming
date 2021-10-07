#!/usr/bin/python3
"""Defines a function that prints a string."""


def say_my_name(first_name, last_name=""):
    """Prints the string My name is <first name>
    followed by the <last name>.
    However, <last name> is optional."""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if first_name == "" and last_name == "":
        raise TypeError("first_name and last_name must be string")

    if len(last_name) == 0:
        print("My name is {:s}".format(first_name))
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
