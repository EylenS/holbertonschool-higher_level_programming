#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == 0:
        return None
    for element in reversed(my_list):
        print("{}".format(element))
