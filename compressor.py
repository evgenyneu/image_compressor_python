import imageio
import math

def norm(vector):
    """
    Parameters
    ----------
    vector : list of floats
        A vector. Also accepts column vectors: [[1], [2], [3]].

    Returns
    -------
    float
        Returns the norm of a vector.
    """
    if len(vector) == 0:
        raise ValueError(f"Vector is empty.")

    n = len(vector)
    sum = 0

    for i in range(n):
        try:
            # Assume it's a column vector
            if len(vector[i]) == 1:
                value = vector[i][0]
            else:
                raise ValueError(f"Not a column or row vector")

        except TypeError:
            # Must be a row vector
            value = vector[i]

        sum += value**2

    return math.sqrt(sum)

    


def matrix_multiply(a, b):
    """
    Multiplies two matrices.

    Parameters
    ----------
    a, b : list of numbers
        Matrices to multiply.

    Returns
    -------
    list of numbers
        The product of the two matrices.
    """

    if len(a) == 0 or len(b) == 0 or len(b[0]) == 0:
        raise ValueError(f"Supplied matrix is empty.")

    if len(a[0]) != len(b):
        raise ValueError(f"Incompatible dimensions.")

    # We use the following letters for matrix dimensions:
    #   a is m by n,
    #   b is n by p.

    m = len(a)
    n = len(a[0])
    p = len(b[0])
    product = [[0] * p for i in range(m)]

    for i in range(m):
        for j in range(p):
            element = 0

            if len(a[i]) != n:
                raise ValueError(f"Unequal number of elements in rows of a.")

            for k in range(0, n):
                if len(b[k]) != p:
                    raise ValueError(f"Unequal number of elements in columns of b.")

                element += a[i][k] * b[k][j]

            product[i][j] = element

    return product


def load_image(path):
    """
    Loads image and returns the data

    Parameters
    ----------
    path : str
        Path to the image file.

    Returns
    -------
    imageio.core.util.Array
        Array containing image data.
    """

    return imageio.imread(path)


if __name__ == '__main__':
    load_image('images/marmite_500x500_gray.bmp')