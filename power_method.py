"""
Calculate eigenvalues and eigenvectors of a matrix using the power method.
"""

from linear_algebra import matrix_size


def eigen_system(matrix, max_eigenvalues):
    """
    Calculates eigenvalues and eigenvectors of a matrix.

    Parameters
    ----------
    matrix : list of floats
        A matrix.

    max_eigenvalues : int
        Maximum number or largest eigenvalues to calculate.

    Returns
    -------
    list of dict
        Array of dictionaries containing distinct eigenvalues with eigenvectors:
        [
            {
                "eigenvalue": -2.0,
                "eigenvectors": [[1, 2, 0]]
            },
            {
                "eigenvalue": 2.0,
                "eigenvectors": [[1, -2, 0], [0, 0, 1]]
            }
        }
        
    """

    row_count, col_count = matrix_size(matrix)

    # Create an initial unit vector
    unit_vector = [0] * col_count
    unit_vector[0] = 1

    return 42
