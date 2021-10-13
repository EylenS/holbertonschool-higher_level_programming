#!/usr/bin/python3
"""This module contains a method
to open and read a file."""


def read_file(filename=""):
    """Reads a text file (UTF8) -filename-
    and prints it to stdout."""

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
