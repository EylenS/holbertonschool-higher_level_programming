#!/usr/bin/python3
"""
Defines MyList class.
"""


class MyList(list):
    """A subclass of list class."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
