"""
Singular value decomposition and expansion.
"""

from linear_algebra import matrix_multiply, matrix_scalar_multiply, gramian, transpose, matrix_add
from power_method import dominant_eigen_system
import math


def find_u_from_v(matrix, v, singular_value):
    """
    Finds the u column vector of the U matrix in the SVD UΣV^T.

    Parameters
    ----------
    matrix : list of list of float
        Matrix for which the SVD is calculated

    v : list of list of float
        A column vector of V matrix, it is the eigenvector of the Gramian of `matrix`.

    singular_value : float
        A singular value of `matrix` corresponding to the `v` vector.

    Returns
    -------
    list of list of floats
        u column vector of the U matrix in the SVD.
    """

    return matrix @ v / singular_value


def svd(matrix, max_eigenvalues, iterations):
    """
    Performs reduced singular value decomposition of the matrix.

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

        if eigenvalue == 0:
            break

        singular_value = math.sqrt(eigenvalue)
        u = find_u_from_v(matrix, v=v, singular_value=singular_value)
        svd_items.append((u, singular_value, v))

        if iteration == (max_eigenvalues - 1):
            break

        # Calculate the negative of the first dominant term of the singular value expansion
        dominant = matrix_multiply(u, transpose(v))
        dominant = matrix_scalar_multiply(dominant, -singular_value)

        # Subtract the dominant term
        matrix = matrix_add(matrix, dominant)

    return svd_items


def singular_value_expansion(data):
    """
    Performs singular value expansion by reconstructing the original `matrix`
    from its SVD UΣV^T.

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
        Matrix reconstructed form its SVD UΣV^T.
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

