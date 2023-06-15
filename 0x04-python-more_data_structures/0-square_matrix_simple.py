#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    """Squares the values of a 2 dimensional matrix

        Args:
        matrix: 2 dimentional matrix

        Returns:
        Returns a 2 dimensional matrix with squared values
     """
    new_matrix = []
    for row in matrix:
        tmp = []
        for col in row:
            tmp.append(col * col)
        new_matrix.append(tmp.copy())
        tmp.clear()
    return new_matrix
