#!/usr/bin/python3
"""Defines a module that prints the shape of a square."""


def print_square(size):
    """Prints a square with the character '#'."""

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
