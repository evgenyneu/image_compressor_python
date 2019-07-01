import imageio
from svd import svd
import numpy as np


def compress_image(path):
    data = load_image(path)

    svd_data = svd(matrix=data, max_eigenvalues=3, iterations=10)

    # print(f"len(svd_data): {len(svd_data)}")
    return 12


def load_image(path):
    """
    Loads image and returns the data

    Parameters
    ----------
    path : str
        Path to the image file.

    Returns
    -------
    numpy.ndarray
        Array containing image data.
    """

    return np.array(imageio.imread(path))


if __name__ == '__main__':
    load_image('images/marmite_500x500_gray.bmp')
