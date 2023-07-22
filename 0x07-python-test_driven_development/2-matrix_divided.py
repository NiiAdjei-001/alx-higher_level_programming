#!/usr/bin/python3
"""Divide Matrix Module
"""


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
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for r in range(len(matrix)):
        temp = []
        if r > 0 and len(matrix[r]) != len(matrix[r-1]):
            raise TypeError("Each row of the matrix must have the same size")
        for c in range(len(matrix[r])):
            if not (type(matrix[r][c]) in [int, float]):
                raise TypeError(
                        "{}{}".format("matrix must be a matrix ",
                                      "(list of lists) of integers/floats"))
            temp.append(round(matrix[r][c]/div, 2))
        result.append(temp)
    return result
