#!/usr/bin/python3
"""Divide all elements of a matrix

args: matrix, div

"""


def matrix_divided(matrix, div):
    """
    Divides elements of a matrix
    """
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"
    error3 = "div must be a number"
    error4 = "division by zero"
    list_len = len(matrix[0])

    if type(div) != int and type(div) != float:
        raise TypeError(error3)
    if div == 0:
        raise ZeroDivisionError(error4)

    new = [[]]

    for row in matrix:
        if len(row) != list_len:
            raise TypeError(error2)
        for column in row:
            if type(column) != int and type(column) != float:
                raise TypeError(error1)

        new = [[round(col / div, 2) for col in r] for r in matrix]

    return new
