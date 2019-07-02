from annotate import annotate
from shutil import copyfile
import os


def test_annotate():
    path = 'images/for_compression/marmite_500x500.jpg'
    path_annotated = 'images/for_compression/marmite_500x500_annotated.jpg'
    copyfile(path, path_annotated)
    annotate(path_annotated, terms=10, compression=12.2, fontsize=30)
    assert os.path.exists(path_annotated)
    os.remove(path_annotated)
