#!/usr/bin/python3
"""This module handle a method that appends a string at
the end of a text file ."""


def append_write(filename="", text=""):
    """This fun appends a string at the end of a text file
    and returns the number of characters added"""

    with open(filename, 'a', encoding='utf-8') as f:
        n_chars = f.write(text)
        return n_chars
