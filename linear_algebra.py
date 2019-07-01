"""
Linear algebra functions (matrix multiplication, vector length etc.)
"""

import math
import copy
import numpy as np


def gramian(matrix):
    """
    Parameters
    ----------
    matrix : list
        A matrix

    Returns
    -------
    list
        The Gramian of `matrix`.
    """

    return matrix_multiply(transpose(matrix), matrix)


def dot_product(vector1, vector2):
    """
    Calculates a dot product of two vectors

    Parameters
    ----------
    vector1, vector2 : list
        Two n by 1 matrices.

    Returns
    -------
    float
        The dot product of two matrices
    """

    row_count1, col_count1 = matrix_size(vector1)
    row_count2, col_count2 = matrix_size(vector2)

    if row_count1 != row_count2:
        raise ValueError(f"Incompatible dimensions.")

    if col_count1 != 1 or col_count2 != 1:
        raise ValueError(f"Matrices should be n by 1.")

    sum = 0

    for i in range(row_count1):
        sum += vector1[i][0] * vector2[i][0]

    return sum


def transpose(matrix):
    """
    Transposes a matrix.

    Parameters
    ----------
    matrix : list
        A matrix.

    Returns
    -------
    list
        Transposed matrix.
    """

    row_count, col_count = matrix_size(matrix)

    transposed = [[0] * row_count for i in range(col_count)]

    for i in range(row_count):
        for j in range(col_count):
            transposed[j][i] = matrix[i][j]

    return transposed


def matrix_size(matrix):
    """
    Parameters
    ----------
    matrix : list of floats
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


def norm(vector):
    """
    Parameters
    ----------
    vector : numpy.ndarray
        A vector.

    Returns
    -------
    float
        Vector's length.
    """

    return np.linalg.norm(vector)


def matrix_add(a, b):
    """
    Add two matrices.

    Parameters
    ----------
    a, b : numpy.ndarray
        Matrices to multiply.

    Returns
    -------
    numpy.ndarray
        The product of the two matrices.
    """

    return np.add(a, b)


def matrix_multiply(a, b):
    """
    Multiplies two matrices.

    Parameters
    ----------
    a, b : numpy.ndarray
        Matrices to multiply.

    Returns
    -------
    numpy.ndarray
        The product of the two matrices.
    """

    # We use the following letters for matrix dimensions:
    #   a is m by n,
    #   b is n by p.

    m, n = matrix_size(a)
    b_n, p = matrix_size(b)

    if n != b_n:
        raise ValueError(f"Incompatible dimensions.")

    return np.dot(a, b)


def matrix_scalar_multiply(matrix, scalar):
    """
    Multiplies a matrix with a scalar.

    Parameters
    ----------
    matrix : numpy.ndarray
        Matrix to be multiplied by the scalar.

    scalar : flat
        A scalar.

    Returns
    -------
    numpy.ndarray
        Matrix, the result of the matrix-scalar multiplication.
    """

    return np.multiply(scalar, matrix)
