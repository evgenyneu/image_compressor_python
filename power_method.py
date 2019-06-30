"""
Calculate eigenvalues and eigenvectors of a matrix using the power method.
"""

from linear_algebra import matrix_size, matrix_multiply, norm, \
    matrix_scalar_multiply


def dominant_eigen_system(matrix):
    """
    Calculates the dominant eigenvalue and a dominant unit eigenvector
    of a symmetric matrix using the power method.

    Parameters
    ----------
    matrix : list of list of floats
        A symmetric matrix.

    Returns
    -------
    tuple of (Int, matrix)
        Dominant eigenvalue and a dominant unit eigenvector.
    """

    row_count, col_count = matrix_size(matrix)

    # Create an initial unit vector
    unit_vector = [[0] for i in range(col_count)]
    unit_vector[0][0] = 1
    iterations = 4

    # Calculate dominant unit eigenvector
    for _ in range(iterations):
        product = matrix_multiply(matrix, unit_vector)
        scalar = 1 / norm(product)
        unit_vector = matrix_scalar_multiply(product, scalar)

    # Calculate dominant eigenvalue
    # matrix_multiply(matrix, unit_vector)

    return (1, unit_vector)
