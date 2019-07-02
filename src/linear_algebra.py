"""
Linear algebra functions (matrix multiplication, vector length etc.)
"""

import numpy as np


def gramian(matrix):
    """
    Parameters
    ----------
    matrix : numpy.ndarray
        A matrix

    Returns
    -------
    numpy.ndarray
        The Gramian of `matrix`.
    """

    return np.transpose(matrix) @ matrix


def dot_product(vector1, vector2):
    """
    Calculates a dot product of two vectors.

    Parameters
    ----------
    vector1, vector2 : numpy.ndarray
        Two n by 1 matrices.

    Returns
    -------
    float
        The dot product of two matrices
    """

    return np.dot(np.transpose(vector1), vector2)[0, 0]


def matrix_size(matrix):
    """
    Parameters
    ----------
    matrix : numpy.ndarray
        A matrix.

    Returns
    -------
    tuple of two integers
        Size of a matrix. First integer is the number of rows.
    """

    rows = len(matrix)

    if rows > 0:
        columns = len(matrix[0])
    else:
        columns = 0

    return (rows, columns)
