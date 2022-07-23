#!/usr/bin/python3
"""
This is the "Matrix Divided" module.

The matrix Divided module takes in a list of lists matrix and divisor.
All valid elements are divided by the divisor and returned as new matrix
"""


def matrix_divided(matrix, div):
    """Return a new matrix with all values divided by `div`.
    Matrix must be a list of lists.
    Each sublist must contain only integers or floats.
    Empty sublists are not allowed.
    Divisor must be greater than 0 and must be an int or fload.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(element) > 0 for element in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(element) == len(matrix[0]) for element in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for element in matrix:
        if not isinstance(element, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if not all(isinstance(x, (int, float)) for x in element):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

    if div == 0:
        if isinstance(div, bool):
            raise TypeError("div must be a number")
        raise ZeroDivisionError("division by zero")
    if isinstance(div, bool):
        raise TypeError("div must be a number")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = []
    for element in matrix:
        new_matrix.append(list(map(lambda n: round(n / div, 2), element)))

    return new_matrix
