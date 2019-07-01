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


def svd(matrix, max_eigenvalues, iterations):
    """
    Performs singular value decomposition of the matrix.

    Parameters
    ----------
    matrix : list
        A matrix.

    max_eigenvalues : int
        Maximum number of eigenvalues to calculate.

    iterations : int
        The number of iterations of the power method.

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
        eigenvalue, v = dominant_eigen_system(matrix_gramian, iterations=iterations)

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


def singular_value_expansion(data):
    """
    Performs singular value expansion by reconstructing the original `matrix`:
        matrix = U Σ V^T.

    Parameters
    ----------
    data : list of tuples
        List of tuples produced by `svd` function: (u, sigma, v), where
            `u` is a column vector of U matrix,
            `sigma` is the corresponding singular value of `matrix`,
                which are the diagonal entries of Σ matrix,
            `v` is a column vector of V matrix
        in `matrix = U Σ V^T` svd.

    Returns
    -------
    list
        Matrix, which is the product of svd U Σ V^T.
    """

    if len(data) == 0:
        return

    size = len(data[0][0])

    matrix = [[0] * size for i in range(size)]

    for data_item in data:
        u = data_item[0]
        singular_value = data_item[1]
        v = data_item[2]

        product = matrix_multiply(u, transpose(v))
        product = matrix_scalar_multiply(product, singular_value)
        matrix = matrix_add(matrix, product)

    return matrix



