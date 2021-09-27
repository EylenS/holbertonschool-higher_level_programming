#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            res = 0
        except (ZeroDivisionError):
            print("division by 0")
            res = 0
        except (IndexError):
            print("out of range")
        finally:
            newList.append(res)
            res = 0
    return newList
