"""
Calculate eigenvalues and eigenvectors of a matrix using the power method.
"""

from linear_algebra import matrix_size, matrix_multiply, norm, \
    matrix_scalar_multiply, dot_product, gramian, transpose, matrix_add

from svd import find_u_from_v
import math


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


def svd(matrix, max_eigenvalues):
    """
    Performs singular value decomposition of the matrix.

    Parameters
    ----------
    matrix : list
        A matrix.

    max_eigenvalues : int
        Maximum number of eigenvalues to calculate.

    Returns
    -------
    list of tuples (list, float, list)
        List of tuples (u, sigma, v), where
            `u` is a column vector of U matrix,
            `sigma` is the corresponding singular value of `matrix`,
                which are the diagonal entries of Σ matrix,
            `v` is a column vector of V matrix
        in `matrix = U Σ V^T` svd.
    """

    svd_items = []

    for iteration in range(max_eigenvalues):
        matrix_gramian = gramian(matrix)
        eigenvalue, v = dominant_eigen_system(matrix_gramian, 10)

        if iteration == (max_eigenvalues):
            break

        singular_value = math.sqrt(eigenvalue)
        u = find_u_from_v(matrix, v=v, singular_value=singular_value)
        svd_items.append((u, singular_value, v))

        # Calculate the negative of the first dominant term of the singular value expansion
        dominant = matrix_multiply(u, transpose(v))
        dominant = matrix_scalar_multiply(dominant, -singular_value)

        # Subtract the dominant term
        matrix = matrix_add(matrix, dominant)

    return svd_items
