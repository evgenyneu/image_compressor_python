"""
Linear algebra functions (matrix multiplication etc.)
"""

import math
import copy

def matrix_size(matrix):
    """
    Parameters
    ----------
    matrix : list of floats
        A matrix.

    Returns
    -------
    tuple of two integers
        Returns the size of a matrix. First integer is the number of rows. Raises exception if rows have unequal number of elements.
    """

    rows = len(matrix)

    if rows == 0:
        columns = 0
    else:
        try:
            columns = len(matrix[0])

            # Check all rows have the same number of elements
            for irow in range(rows):
                current_columns = len(matrix[irow])

                if current_columns != columns:
                    raise ValueError(f"Matrix rows have different number of elements.") 
    
        except TypeError:
            # Must be a row vector
            columns = len(matrix)
            rows = 1
    
    return (rows, columns)

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

    row_count, col_count = matrix_size(vector)
    
    if row_count == 0 or col_count == 0:
        raise ValueError(f"Vector is empty.")

    if row_count != 1 and col_count != 1:
        raise ValueError(f"Not a vector.")

    sum = 0

    for i in range(row_count):
        for j in range(col_count):
            try:
                # Assume it's a 2d list
                value = vector[i][j]
                
            except TypeError:
                # Must be a simple list (a row vector)
                value = vector[j]

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

    # We use the following letters for matrix dimensions:
    #   a is m by n,
    #   b is n by p.

    m, n = matrix_size(a)
    b_n, p = matrix_size(b)

    if m == 0 or n == 0 or p == 0:
        raise ValueError(f"Supplied matrix is empty.")

    if n != b_n:
        raise ValueError(f"Incompatible dimensions.")

    product = [[0] * p for i in range(m)]

    for i in range(m):
        for j in range(p):
            element = 0

            for k in range(0, n):
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

    row_count, col_count = matrix_size(result)
    
    if row_count == 0 or col_count == 0:
        raise ValueError(f"Matrix is empty.")

    for i in range(row_count):
        for j in range(col_count):
            try:
                result[i][j] *= scalar 
            except TypeError:
                # Must be a value of a row vector
                result[j] *= scalar

    return result