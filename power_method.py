"""
Calculating eigenvalues and eigenvectors of a matrix using the power method.
"""

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



    return 42