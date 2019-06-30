"""
Calculate eigenvalues and eigenvectors of a matrix using the power method.
"""

from linear_algebra import matrix_size, matrix_multiply, norm, \
    matrix_scalar_multiply, dot_product, gramian, transpose

from svd import find_u_from_v
import math


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


def eigen_system(matrix, max_eigenvalues):
    """
    Parameters
    ----------
    matrix : list of list of floats
        A symmetric matrix.

    max_eigenvalues : int
        The maximum number of eigenvalues to calculate.

    Returns
    -------
    list of tuples (float, list)
        List of eigenvalues and eigenvectors of the `matrix`.
    """

    matrix_gramian = gramian(matrix)
    eigenvalue, eigenvector = dominant_eigen_system(matrix_gramian, 10)
    singular_value = math.sqrt(eigenvalue)

    u = find_u_from_v(matrix, v=eigenvector, singular_value=singular_value)

    # Calculate the first dominant term of the singular value expansion
    dominant_submatrix = matrix_multiply(u, transpose(eigenvector))
    dominant_submatrix = matrix_scalar_multiply(dominant_submatrix, -singular_value)

    # Subtract the dominant term
    # matrix_add(matrix, dominant_submatrix)

    return 234
