import imageio
import numpy as np


def make_grayscale(input, output):
    """
    Converts image to a grayscale.

    Parameters
    ----------
    input : str
        Path to input image file in BMP, JPG or PNG format.

    output : str
        Path to output grayscale image file.
    """

    # Makes a grayscale image from a colored one
    image = imageio.imread(input)
    rgb = np.array(image)

    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b  # https://stackoverflow.com/q/12201577/297131
    gray = gray.astype(np.uint8)
    imageio.imwrite(output, gray)
