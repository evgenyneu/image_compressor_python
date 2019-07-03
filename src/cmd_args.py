import argparse


def parse_cmd_args(args):
    """
    Parses command line arguments

    Returns
    -------
    argparse.Namespace
        Object containing the values of command line options.
    """

    parser = argparse.ArgumentParser(
        prog="python compress.py",
        description="Compress an image using singular value decomposition.")

    parser.add_argument('IMAGE', help='Path to the image to compress')

    parser.add_argument('--output', help='Path to the compressed image that will be created')

    parser.add_argument(
        '--notext',
        dest="annotate",
        action='store_false',
        help='Do not put text on the image.')

    parser.add_argument(
        '--terms',
        type=int,
        help='Number of terms in the singular value expansion.')

    parser.add_argument(
        '--iterations',
        type=int,
        help='Number of iterations of the power method.')

    return parser.parse_args(args)