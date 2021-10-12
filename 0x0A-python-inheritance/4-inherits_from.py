#!/usr/bin/python3
"""Defines a fun that evaluates if the object
inherits from class or subclass."""


def inherits_from(obj, a_class):
    """Evaluates if the object is an instance of a class that
    inherited (directly or indirectly).
    Returns:
        True: if the object is an instance of a class that inherited
        (directly or indirectly) from a_class.
        Fale: otherwise."""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
