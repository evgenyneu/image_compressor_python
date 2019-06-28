import imageio


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