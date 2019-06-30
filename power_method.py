"""
Calculate eigenvalues and eigenvectors of a matrix using the power method.
"""

from linear_algebra import matrix_size, matrix_multiply, norm, \
    matrix_scalar_multiply, dot_product


def dominant_eigen_system(matrix, iterations):
    """
    Calculates the dominant eigenvalue and a dominant unit eigenvector
    of a symmetric matrix using the power method.

    Parameters
    ----------
    matrix : list of list of floats
        A symmetric matrix.

    iterations : int
        The number of iterations of the power method.

    Returns
    -------
    tuple of (Int, matrix)
        Dominant eigenvalue and a dominant unit eigenvector.
    """

    row_count, col_count = matrix_size(matrix)

    # Create an initial unit vector
    unit_vector = [[0] for i in range(col_count)]
    unit_vector[0][0] = 1

    # Calculate dominant unit eigenvector
    for _ in range(iterations):
        product = matrix_multiply(matrix, unit_vector)
        scalar = 1 / norm(product)
        unit_vector = matrix_scalar_multiply(product, scalar)

    # Calculate dominant eigenvalue
    eigenvalue = dot_product(matrix_multiply(matrix, unit_vector), unit_vector)

    return (eigenvalue, unit_vector)
