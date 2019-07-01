"""
Calculate eigenvalues and eigenvectors of a matrix using the power method.
"""

from linear_algebra import matrix_size, matrix_multiply, norm, \
    matrix_scalar_multiply, dot_product

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
    unit_vector = [[0] for i in range(col_count)]
    unit_vector[0][0] = 1

    # Calculate dominant unit eigenvector
    for _ in range(iterations):
        product = matrix_multiply(matrix, unit_vector)
        vec_length = norm(product)

        # Reached zero eigenvalue
        if vec_length < ZERO_NUMBER:
            return (0, [])

        scalar = 1 / vec_length
        unit_vector = matrix_scalar_multiply(product, scalar)

    # Calculate dominant eigenvalue
    eigenvalue = dot_product(matrix_multiply(matrix, unit_vector), unit_vector)

    return (eigenvalue, unit_vector)
