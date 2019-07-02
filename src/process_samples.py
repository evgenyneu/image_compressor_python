"""
Compresses sample images of different size using different number of terms
in singular value expansion.
"""

import os
import imageio
from core import load_image, image_size, compression_ratio, compress_image, compressed_image_path


def process(silent=False, only_widths=[]):
    """
    Compresses sample images of different size using different number of terms in
    singular value expansion.

    Parameters
    ----------
    silent : bool
        Does not show any output when True.

    only_widths : list of int
        If the list is not empty, process only images that have given widths.
    """

    dirname = 'images/for_compression/'
    out_subdir = 'images/compressed/'
    filenames = os.listdir(dirname)

    if not silent:
        print("Creating images:")

    for filename in filenames:
        if not filename.endswith(".jpg"):
            continue

        path = os.path.join(dirname, filename)
        data = load_image(path)
        width, height = image_size(data)
        size_test = f"{width}x{height}"

        if len(only_widths) > 0 and width not in only_widths:
            continue

        for terms in [1, 2, 5, 10, 20, 50, 100, 150, 200, 300, 500]:
            outdir = os.path.join(out_subdir, size_test)

            if not os.path.exists(outdir):
                os.makedirs(outdir)

            ratio = compression_ratio(width=width, height=height, terms=terms)

            if ratio > 1.2:
                continue

            path_out = compressed_image_path(path, width=width, height=height, terms=terms,
                                             outdir=outdir)

            if not silent:
                print(path_out)

            result = compress_image(data, terms=terms)
            compressed_data = result['compressed_data']
            imageio.imwrite(path_out, compressed_data)

    if not silent:
        print("Done")
