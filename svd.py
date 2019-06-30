from linear_algebra import matrix_multiply, matrix_scalar_multiply


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

    product = matrix_multiply(matrix, v)
    return matrix_scalar_multiply(product, 1 / singular_value)
