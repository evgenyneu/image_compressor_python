import imageio
from svd import svd, singular_value_expansion
import numpy as np


def compress_image(path, path_out, terms, iterations):
    data = load_image(path)

    svd_data = svd(matrix=data, max_eigenvalues=terms, iterations=iterations)
    compressed_data = singular_value_expansion(svd_data)

    # Save to image
    compressed_data = np.clip(compressed_data, 0, 254)
    compressed_data = compressed_data.astype(np.uint8)
    imageio.imwrite(path_out, compressed_data)


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
