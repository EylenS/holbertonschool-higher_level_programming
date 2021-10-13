#!/usr/bin/python3
"""This module contains a function that deserializing JSON."""


import json


def from_json_string(my_str):
    """This fun function that returns an object (Python data
    structure) represented by a JSON string."""
    return (json.loads(my_str))
