#!/usr/bin/python3
def number_Squared(number):
    return number**2


def square_matrix_simple(matrix=[]):
    newMatrix = matrix[:]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            newMatrix[i] = list(map(number_Squared, matrix[i]))
    return newMatrix
