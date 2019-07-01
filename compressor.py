import imageio
from svd import svd, singular_value_expansion
import numpy as np


def compress_image(path, path_out, terms):
    iterations = iterations_for_terms(terms)
    data = load_image(path)

    if data.ndim == 2:  # Black and white image
        data = np.expand_dims(data, axis=2)

    compressed = np.empty((data.shape[0], data.shape[1], 0))

    # Iterate over each of the colors
    for i in range(data.shape[-1]):
        color_data = data[:, :, i]

        # Compress the data for the color
        svd_data = svd(matrix=color_data, max_eigenvalues=terms, iterations=iterations)
        compressed_data = singular_value_expansion(svd_data)

        # Convert data values to integers in range between 0 and 254 (brightness)
        compressed_data = np.clip(compressed_data, 0, 254)
        compressed_data = compressed_data.astype(np.uint8)
        compressed_data = np.expand_dims(compressed_data, axis=2)
        compressed = np.append(compressed, compressed_data, axis=2)

    imageio.imwrite(path_out, compressed)


def compression_ratio(width, height, terms):
    """
    Parameters
    ----------
    width : int
        Width of the image in pixels.

    height : int
        Width of the image in pixels.

    terms : int
        The number of terms in the singular value expansion.

    Returns
    -------
    float
        The of the compressed image relative to non-compressed.
    """

    return terms * (1 + width + height) / (width * height)


def iterations_for_terms(terms):
    """
    Parameters
    ----------
    terms : int
        Number of terms in the singular value expansion.

    Returns
    -------
    Int
        The number of iterations of the power method needed to produce
        reasonably good image qualit for the given number of terms in the singular value expansion.
        By "reasonably good" we mean that using larger number of terms will not produce noticeably
        better image, thus it is wasteful.
    """

    if terms <= 20:
        return 10

    if terms <= 50:
        return 5

    if terms <= 100:
        return 3

    return 1


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
