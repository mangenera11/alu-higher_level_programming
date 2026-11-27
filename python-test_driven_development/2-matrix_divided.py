#!/usr/bin/python3
"""Module 2-matrix_divided.

Provides matrix_divided(), which divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with every element divided by div.

    matrix must be a non-empty list of non-empty lists of integers or
    floats, all of the same size. div must be a non-zero number. Each
    result is rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(msg)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
