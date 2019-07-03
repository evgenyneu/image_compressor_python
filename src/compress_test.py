from compress import compress
import os


def test_compress():
    path = "images/for_compression/marmite_100x100.jpg"

    result = compress(path=path, path_out=None, terms=None, annotate=False, silent=False)

    output_path = result['output_path']
    assert output_path == 'images/for_compression/marmite_100x100_10_terms_5.0x_compression.jpg'
    assert os.path.exists(output_path)
    os.remove(output_path)
    