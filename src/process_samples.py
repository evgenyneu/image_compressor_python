"""
Compresses sample images of different size using different number of terms
in singular value expansion.
"""

import os
import sys
import imageio
from core import load_image, image_size, compression_ratio, compress_image, compressed_image_path
from annotate import annotate_from_width


def process(dirname, out_subdir, silent=False, only_widths=[]):
    """
    Compresses sample images from `dirname` using different number of terms in
    singular value expansion.

    Parameters
    ----------
    dirname : string
        Path to directory for the images to process.

    out_subdir : string
        Path to directory where the compressed images will be created.

    silent : bool
        Does not show any output when True.

    only_widths : list of int
        If the list is not empty, process only images that have given widths.
    """

    filenames = os.listdir(dirname)

    if not silent:
        print("Creating images:")

    supported_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]

    for filename in filenames:
        _, file_extension = os.path.splitext(filename)
        if file_extension.lower() not in supported_extensions:
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
            annotate_from_width(path=path_out, terms=terms, width=width, ratio=ratio)

    if not silent:
        print("Done")


def process_with_args(args):
    if len(args) != 2:
        print("Incorrect arguments.\n")
        print("Usage:")
        print("   $ python src/process_samples.py INPUT_DIR OUTPUT_DIR\n")
        print("Replace `INPUT_DIR` with the name of directory \
            that contains images you want to compress, in JPG, PNG or BMP format. \
            All images in the directory will be compressed.\n")
        print("Replace `OUTPUT_DIR` with a name of the directory where you want \
            compressed images to be placed.")
        return

    process(dirname=args[0], out_subdir=args[1])


if __name__ == '__main__':
    process_with_args(sys.argv[1:])
