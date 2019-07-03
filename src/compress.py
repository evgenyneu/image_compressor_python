from cmd_args import parse_cmd_args
from core import compress_image_to_file
import sys

DEFAULT_TERMS = 10  # Default number of terms in the singular value expansion


def compress(path, path_out, terms, annotate):
    if terms is None:
        terms = DEFAULT_TERMS

    return compress_image_to_file(path=path, terms=terms, path_out=path_out)


if __name__ == '__main__':
    cmd_options = parse_cmd_args(sys.argv[1:])

    compress(
        path=cmd_options.IMAGE,
        path_out=cmd_options.output,
        terms=cmd_options.terms,
        annotate=cmd_options.annotate
    )
