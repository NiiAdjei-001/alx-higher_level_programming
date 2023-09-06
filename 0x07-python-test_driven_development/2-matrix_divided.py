#!/usr/bin/python3
"""Divide Matrix Module
"""


te0 = "div must be a number"
zde0 = "division by zero"
te1 = "matrix must be a matrix (list of lists) of integers/floats"
te2 = "Each row of the matrix must have the same size"
te3 = "matrix must be a matrix (list of lists) of integers/floats"


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a value

        Args
            matrix: a list of list of integers/floats (matrix)
            div: an integer /float that will be the divisor

            Return:
            returns a matrix of divided elements
    """
    result = []
    if not type(div) in [int, float]:
        raise TypeError(te0)
    if div == 0:
        raise ZeroDivisionError(zde0)
    if type(matrix) != list:
        raise TypeError(te1)
    for r in range(len(matrix)):
        temp = []
        if r > 0 and len(matrix[r]) != len(matrix[r-1]):
            raise TypeError(te2)
        for c in range(len(matrix[r])):
            if not (type(matrix[r][c]) in [int, float]):
                raise TypeError(te3)
            temp.append(round(matrix[r][c] / div, 2))
        result.append(temp)
    return result
