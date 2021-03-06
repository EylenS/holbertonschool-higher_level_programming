#!/usr/bin/python3
"""Defines a division operation of all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides each of the elements of a matrix."""

    str = "matrix must be a matrix (list of lists) of integers/floats"
    str_row = "Each row of the matrix must have the same size"
    newList = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(str)

    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(str)

        internalList = []
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int and type(matrix[i][j]) is not float:
                raise TypeError(str)
            if len(matrix[0]) != len(matrix[i]):
                raise TypeError(str_row)
            internalList.append(round(matrix[i][j] / div, 2))
        newList.append(internalList)
    return newList
