#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    """Squares the values of a 2 dimensional matrix

        Args:
        matrix: 2 dimentional matrix

        Returns:
        Returns a 2 dimensional matrix with squared values
     """
    r_len = len(matrix)
    squares = []
    for row in range(0, r_len):
        c_len = len(matrix[row])
        temp = []
        for col in range(0, c_len):
            temp.append(matrix[row][col] ** 2)
        squares.append(temp.copy())
        temp.clear()
    return squares
