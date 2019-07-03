from cmd_args import parse_cmd_args
from core import compress_image_to_file
import sys

DEFAULT_TERMS = 10  # Default number of terms in the singular value expansion


def compress(path, path_out, terms, annotate, silent):
    if terms is None:
        terms = DEFAULT_TERMS

    if not silent:
        print(f"Compressing image...")

    result = compress_image_to_file(path=path, terms=terms, path_out=path_out)

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
        annotate=cmd_options.annotate,
        silent=False
    )
