from cmd_args import parse_cmd_args
from core import compress_image_to_file
import sys

DEFAULT_TERMS = 10  # Default number of terms in the singular value expansion


def compress(path, path_out, terms, iterations, annotate, silent):
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

    iterations : int
        The number of iterations of the power method.
        If None, the optimal number is determined automatically.

    annotate : bool
        If True, a text is added on top of the image,
        describing compression level and the `terms` settings used.

    silent : bool
        If True, the program does not produce any text output.

    Returns
    -------
    dict
        The dictionary containing compressed data, the number of iteration used,
        the output path and compression ratio:
        {
            'compressed_data': data,
            'iterations': 10,
            'output_path': ' /dir/image.jpg',
            'compression_ratio': 5.7
        }
    """
    if terms is None:
        terms = DEFAULT_TERMS

    if not silent:
        print(f"Compressing image...")

    result = compress_image_to_file(path=path, terms=terms,
                                    iterations=iterations,
                                    path_out=path_out,
                                    annotate=annotate)

    output_path = result['output_path']

    if not silent:
        print(f"Compressed to:\n{output_path}")
        print(f"Terms in singular value expansion: {terms}")
        print(f"Power method iterations: {result['iterations']}")
        print(f"Compression ratio: {result['compression_ratio']}")

    return result


if __name__ == '__main__':
    cmd_options = parse_cmd_args(sys.argv[1:])

    compress(
        path=cmd_options.IMAGE,
        path_out=cmd_options.output,
        terms=cmd_options.terms,
        iterations=cmd_options.iterations,
        annotate=cmd_options.annotate,
        silent=False
    )
