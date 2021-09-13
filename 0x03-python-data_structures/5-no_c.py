#!/usr/bin/python3
def no_c(my_string):
    joker = ""
    for idx in my_string:
        if idx != "c" and idx != "C":
            joker = joker + idx
    return joker
