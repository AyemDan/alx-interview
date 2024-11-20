#!/usr/bin/python3
"""
Matrix rotation
"""
def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.

    Parameters:
    -----------
    matrix : List[List[int]]
        A 2D list representing the matrix to be rotated. It is assumed to be
        a square matrix (n x n).

    How it works:
    -------------
    1. Transpose the matrix:
       - Swap elements across the diagonal (matrix[i][j] with matrix[j][i]).
       - This step converts rows into columns.

    2. Reverse each row:
       - After transposing, reversing each row gives the matrix a 90-degree
         clockwise rotation.

    The function modifies the matrix in place and does not return anything.
    """
    n = len(matrix)  # Get the size of the square matrix

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):  # Start j from i to avoid redundant swaps
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
