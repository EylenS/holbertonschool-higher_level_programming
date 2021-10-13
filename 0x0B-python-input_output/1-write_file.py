#!/usr/bin/python3
"""This module handle a method that writes
a string to a text file."""


def write_file(filename="", text=""):
    """This function: write(s) -> writes the string <s>
    to the file and returns the number of characters written."""

    with open(filename, 'w', encoding='utf-8') as f:
        n_chars = f.write(text)
        return n_chars
