"""
Functions that perform linear algebra operations, like matrix multiplication.
"""

import math
import copy

def norm(vector):
    """
    Parameters
    ----------
    vector : list of floats
        A vector. Also accepts column vectors: [[1], [2], [3]].

    Returns
    -------
    float
        Returns vector's length.
    """
    if len(vector) == 0:
        raise ValueError(f"Vector is empty.")

    n = len(vector)
    sum = 0

    for i in range(n):
        try:
            # Assume it's a column vector
            if len(vector[i]) == 1:
                value = vector[i][0]
            else:
                raise ValueError(f"Not a column or row vector")

        except TypeError:
            # Must be a row vector
            value = vector[i]

        sum += value**2

    return math.sqrt(sum)

def matrix_multiply(a, b):
    """
    Multiplies two matrices.

    Parameters
    ----------
    a, b : list of numbers
        Matrices to multiply.

    Returns
    -------
    list of numbers
        The product of the two matrices.
    """

    if len(a) == 0 or len(b) == 0 or len(b[0]) == 0:
        raise ValueError(f"Supplied matrix is empty.")

    if len(a[0]) != len(b):
        raise ValueError(f"Incompatible dimensions.")

    # We use the following letters for matrix dimensions:
    #   a is m by n,
    #   b is n by p.

    m = len(a)
    n = len(a[0])
    p = len(b[0])
    product = [[0] * p for i in range(m)]

    for i in range(m):
        for j in range(p):
            element = 0

            if len(a[i]) != n:
                raise ValueError(f"Unequal number of elements in rows of a.")

            for k in range(0, n):
                if len(b[k]) != p:
                    raise ValueError(f"Unequal number of elements in columns of b.")

                element += a[i][k] * b[k][j]

            product[i][j] = element

    return product

def matrix_scalar_multiply(matrix, scalar):
    """
    Multiplies a matrix with a scalar.

    Parameters
    ----------
    matrix : list of float
        Matrix to be multiplied by the scalar.

    scalar : flat
        A scalar.

    Returns
    -------
    list of numbers
        Matrix, the result of the matrix-scalar multiplication.
    """

    # Copy the matrix, we don't want to modify the input matrix
    result = copy.deepcopy(matrix)
    
    if len(result) == 0:
        raise ValueError(f"Matrix is empty.")

    for i in range(len(result)):
        vector_or_number = result[i]

        try:
            # Test if this is a column vector by getting its length
            row_length = len(vector_or_number)

            for j in range(row_length):
                vector_or_number[j] *= scalar
        except TypeError:
            # Must be a value of a row vector
            result[i] *= scalar

    return result