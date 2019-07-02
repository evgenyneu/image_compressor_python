import imageio
from svd import svd, singular_value_expansion
import numpy as np
import os


def compress_image_to_file(path, terms, path_out=None):
    """
    Compresses the image from `path` using singular value expansion.
    The image is saved to an output file which name is chosen automatically,
    unless `path_out` is specified.

    Parameters
    ----------
    path : path
        Path to the image to be compressed.

    path_out : string
        The path where the compressed image will be created.
        If None, the output name is chosen automatically.

    terms : int
        The number of terms in the singular value expansion.

    Returns
    -------
    dict
        The dictionary containing compressed data, the number of iteration used,
        and the output path:
        {
            'compressed_data': data,
            'iterations': 10,
            'output_path': ' /dir/image.jpg'
        }
    """

    data = load_image(path)
    width, height = image_size(data)

    if path_out is None:
        path_out = compressed_image_path(path, width=width, height=height, terms=terms)

    result = compress_image(data, terms=terms)
    compressed_data = result['compressed_data']
    imageio.imwrite(path_out, compressed_data)
    result['output_path'] = path_out
    return result


def compress_image(data, terms, iterations=None):
    """
    Compresses the image from `path` using singular value expansion.

    Parameters
    ----------
    data : numpy.ndarray
        Image data.

    path_out : string
        The path where the compressed image will be created.

    terms : int
        The number of terms in the singular value expansion.

    iterations : int
        Number of terms in the singular value expansion.
        If None, the number is chosen automatically.

    Returns
    -------
    dict
        The dictionary containing compressed data and the number of iteration used:
        {
            'compressed_data': data,
            'iterations': 10
        }
    """

    if iterations is None:
        iterations = iterations_for_terms(terms)

    if data.ndim == 2:  # Black and white image
        data = np.expand_dims(data, axis=2)

    compressed = np.empty((data.shape[0], data.shape[1], 0), dtype=np.uint8)

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

    result = {
                'compressed_data': compressed,
                'iterations': iterations
            }

    return result


def image_size(data):
    """
    Parameters
    ----------
    data : numpy.ndarray
        Image data.

    Returns
    -------
    tuple (int, int)
        Image width and height.
    """

    image_shape = data.shape
    return (image_shape[0], image_shape[1])


def compressed_image_path(path, width, height, terms, outdir=None):
    """
    Parameters
    ----------
    path: string
        Path to the uncompressed image.

    width : int
        Width of the image in pixels.

    height : int
        Width of the image in pixels.

    terms : int
        The number of terms in the singular value expansion.

    Returns
    -------
    string
        Path to the compressed image.
    """

    ratio = compression_ratio(width=width, height=height, terms=terms)
    compression = f"{(1/ratio):0.1f}x_compression"
    terms_text = f"{terms}_terms"
    dirname, filename_without_extension, file_extension = dir_filename_extension(path)

    if outdir is None:
        outdir = dirname

    return f"{outdir}/{filename_without_extension}_{terms_text}_{compression}{file_extension}"


def dir_filename_extension(path):
    """
    Parameters
    ----------
    path : string
        Path to a file.

    Returns
    -------
    tuple of string (string, string, string)
        The base dir, file name without extension and extension.
    """

    filename, file_extension = os.path.splitext(path)
    dirname = os.path.dirname(filename)
    filename_without_extension = os.path.basename(filename)

    return (dirname, filename_without_extension, file_extension)


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


