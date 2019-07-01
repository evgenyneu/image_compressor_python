"""
Calculate eigenvalues and eigenvectors of a matrix using the power method.
"""

from linear_algebra import matrix_size, dot_product

import numpy as np

ZERO_NUMBER = 1e-20  # Values smaller than this numbers are considered to be zero


def dominant_eigen_system(matrix, iterations):
    """
    Calculates the dominant eigenvalue and a dominant unit eigenvector
    of a symmetric matrix using the power method.

    Parameters
    ----------
    matrix : list
        A symmetric matrix.

    iterations : int
        The number of iterations of the power method.

    Returns
    -------
    tuple of (Int, list)
        Dominant eigenvalue and a dominant unit eigenvector.
        The list is empty if the dominant eigenvalue is zero.
    """

    row_count, col_count = matrix_size(matrix)

    # Create an initial unit vector
    unit_vector = np.zeros([col_count, 1])
    unit_vector[0, 0] = 1

    # Calculate dominant unit eigenvector
    for _ in range(iterations):
        product = matrix @ unit_vector
        vec_length = np.linalg.norm(product)

        # Reached zero eigenvalue
        if vec_length < ZERO_NUMBER:
            return (0, [])

        unit_vector = product / vec_length

    # Calculate dominant eigenvalue
    eigenvalue = dot_product(matrix @ unit_vector, unit_vector)

    return (eigenvalue, unit_vector)
