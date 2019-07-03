import argparse


def parse_cmd_args(args):
    parser = argparse.ArgumentParser(
        prog="python compress.py",
        description='Compress an image using singular value decomposition')

    parser.add_argument('IMAGE', help='Path to the image to compress')
    parser.add_argument('DESTINATION', help='Path to the compressed image that will be created')

    parser.add_argument(
        '--annotate',
        action='store_true',
        help='Put the number of terms and compression level in the output image')

    return parser.parse_args(args)