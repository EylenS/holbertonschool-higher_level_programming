#!/usr/bin/python3
"""This module contains a function that
creates an Object from json file"""


import json


def load_from_json_file(filename):
    """This fun creates an Object from a “JSON file”."""

    with open(filename, encoding='utf-8') as json_file:
        newObject = json.loads(json_file.read())
    return newObject
