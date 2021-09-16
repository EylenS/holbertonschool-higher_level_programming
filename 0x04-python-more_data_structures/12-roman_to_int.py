#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    r_i = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    val_ant = 0
    for idx in range(len(roman_string)):
        for key, val in r_i.items():
            if key == roman_string[idx]:
                result += val
                if val_ant < val:
                    result -= (val_ant * 2)
                    val_ant = val
    return result
# val_ant: previous value
