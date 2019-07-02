from process_samples import process
import os


def test_process():
    path = 'images/compressed/100x100/marmite_100x100_1_terms_49.8x_compression.jpg'

    if os.path.exists(path):
        os.remove(path)

    process(silent=True, only_widths=[100])

    assert os.path.exists(path)
