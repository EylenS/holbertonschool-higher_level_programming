#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    keys = list(a_dictionary.keys())
    biggest = keys[0]
    for x in keys:
        biggest = x if a_dictionary[x] > a_dictionary[biggest] else biggest
    return biggest
