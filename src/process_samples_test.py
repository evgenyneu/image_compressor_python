from process_samples import process
import os
import shutil


def test_process():
    path = 'images/compressed_test/100x100/marmite_100x100_1_terms_49.8x_compression.jpg'

    if os.path.exists(path):
        os.remove(path)

    dirname = 'images/for_compression/'
    out_subdir = 'images/compressed_test/'

    process(dirname=dirname, out_subdir=out_subdir, silent=True, only_widths=[100])

    assert os.path.exists(path)
    shutil.rmtree(out_subdir)
