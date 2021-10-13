#!/usr/bin/python3
"""This module has a function that writes JSON to a file."""

import json


def save_to_json_file(my_obj, filename):
    """This fun writes an Object to a text file,
    using a JSON representation."""

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
