import sys
import os
import re


def annotate(args):
    """
    Adds annotations to images compressed by process_samples.py script.
    The annotation includes the compression level and the `terms` settings used.
    """
    if len(args) != 1:
        print("Incorrect arguments.\n")
        print("Usage:")
        print("   $ python src/annotate.py INPUT_DIR\n")
        print("Replace `INPUT_DIR` with the name of directory that contains images  that were created by using process_samples.py secript.\n")
        return

    dirname = args[0]

    filenames = parse_file_names(dirname)

    for filename in filenames:
        name = filename['name']
        terms = filename['terms']
        compression = filename['compression']

        path_to_image = os.path.join(dirname, name)
        annotated_dir = os.path.join(dirname, "annotated")
        output_path = os.path.join(annotated_dir, name)

        if not os.path.exists(annotated_dir):
            os.makedirs(annotated_dir)

        print(output_path)

        if terms == 1:
            terms_word = "term"
        else:
            terms_word = "terms"

        message = f"{terms} {terms_word}, {compression}x compession"
        annotation = f"-pointsize 30 -gravity south -stroke '#000C' -strokewidth 2 -annotate +0+30 '{message}' -stroke none -fill white -annotate +0+30 '{message}'"

        os.system(f"convert {path_to_image} {annotation} {output_path}")


def parse_file_names(dirname):
    """
    Returns
    -------
    list of dict
        Returns information about the compressed images in directory `dirname`:
            * file name,
            * the `terms` parameter used,
            * compression level.
    """
    filenames = os.listdir(dirname)

    supported_extensions = [".jpg", ".jpeg", ".png", ".bmp"]

    filenames_parsed = []

    for filename in filenames:
        _, file_extension = os.path.splitext(filename)
        if file_extension.lower() not in supported_extensions:
            continue

        match = re.search(r'_(?P<term>\d+)_terms_(?P<compression>[\d\.]+)x_compression', filename)

        filename_parsed = {
            'name': filename
        }

        if match:
            groups = match.groupdict()

            if 'term' in groups:
                terms = match.group('term')
                filename_parsed['terms'] = int(terms)

            if 'compression' in groups:
                compression = match.group('compression')
                compression_number = float(compression)
                if compression_number.is_integer():
                   compression_number = int(compression_number)
                filename_parsed['compression'] = compression_number

        filenames_parsed.append(filename_parsed)

    return filenames_parsed


if __name__ == '__main__':
    annotate(sys.argv[1:])