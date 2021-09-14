#!/usr/bin/python3
newList = []


def divisible_by_2(my_list=[]):
    for number in my_list:
        if number % 2 == 0:
            newList.append(True)
        else:
            newList.append(False)
    return newList
