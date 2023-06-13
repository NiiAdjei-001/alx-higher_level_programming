#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integer values

        Args:
        matrix: matrix of integers

        Returns:
        Does not return anything
    """
    for r in range(0,len(matrix)):
        for c in range(0,len(matrix[r])):
            if c == len(matrix[r]) - 1:
                print("{:d}".format(matrix[r][c]), end="")
            else:
                print("{:d} ".format(matrix[r][c]), end="")
        print()
