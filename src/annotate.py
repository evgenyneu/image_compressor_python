import os


def annotate(path, terms, compression, fontsize):
    """
    Adds an annotation to the image.
    The annotation includes the compression level and the `terms` settings used.
    Image Magic's `convert` command needs to be installed on the system.

    Parameters
    ----------
    path: string
        Path to the image.

    terms : int
        The `terms` parameter that was used to compress the image.

    compression : int
        The compression factor.

    fontsize : int
        The font size for the annotation text.
    """

    if terms == 1:
        terms_word = "term"
    else:
        terms_word = "terms"

    message = f"{terms} {terms_word}\n{compression}x compression"
    margin = fontsize
    annotation = f"-pointsize {fontsize} -gravity south -stroke '#000C' \
        -strokewidth 2 -annotate +0+{margin} '{message}' \
        -stroke none -fill white -annotate +0+{margin} '{message}'"

    os.system(f"convert {path} {annotation} {path}")
