from compressor import load_image, compress_image, iterations_for_terms, compression_ratio, compressed_image_path, dir_filename_extension, image_size

import os
import pytest
from pytest import approx


def test_compressed_image_path():
    path = "/dir/images/marmite_750x375.jpg"
    result = compressed_image_path(path, width=750, height=150, terms=8)

    assert result == "/dir/images/marmite_750x375_8_terms_15.6x_compression.jpg"


def test_dir_filename_extension():
    path = "/dir/dir2/my.cat.jpg"
    dirname, filename_without_extension, file_extension = dir_filename_extension(path)

    assert dirname == "/dir/dir2"
    assert filename_without_extension == "my.cat"
    assert file_extension == ".jpg"


def test_compress_image():
    path = "images/for_compression/marmite_750x375.jpg"
    data = load_image(path)
    result = compress_image(data, path=path, terms=10)
    assert result == 'images/for_compression/marmite_750x375_10_terms_25.0x_compression.jpg'
    assert os.path.exists(result)
    os.remove(result)


@pytest.mark.skip(reason="Long test that creates images at different resolutions")
def test_compress_image_color():
    dirname = 'images/for_compression/'
    outdir = 'images/compressed/'
    filenames = os.listdir(dirname)

    for filename in filenames:
        path = os.path.join(dirname, filename)
        data = load_image(path)
        width, height = image_size(data)
        size_test = f"{width}x{height}"

        for terms in [1, 2, 5, 10, 20, 50, 100, 150, 200, 300, 500]:
            out_dir_with_size = os.path.join(outdir, size_test)

            if not os.path.exists(out_dir_with_size):
                os.makedirs(out_dir_with_size)

            ratio = compression_ratio(width=width, height=height, terms=terms)

            if ratio > 1.2:
                continue

            path_out = compress_image(data, path=path, terms=terms, outdir=out_dir_with_size)
            assert os.path.exists(path_out)


def test_compression_ratio():
    result = compression_ratio(width=1000, height=600, terms=10)

    assert result == approx(0.02668333333)


def test_iterations_for_terms():
    assert iterations_for_terms(1) == 10
    assert iterations_for_terms(2) == 10
    assert iterations_for_terms(5) == 10
    assert iterations_for_terms(10) == 10
    assert iterations_for_terms(20) == 10
    assert iterations_for_terms(21) == 5
    assert iterations_for_terms(50) == 5
    assert iterations_for_terms(51) == 3
    assert iterations_for_terms(100) == 3
    assert iterations_for_terms(101) == 1
    assert iterations_for_terms(500) == 1


def test_load_image():
    result = load_image('images/test_3x3_gray.bmp')
    assert result.shape == (3, 3)

    assert result[0][0] == 79
    assert result[0][1] == 59
    assert result[0][2] == 0

    assert result[1][0] == 149
    assert result[1][1] == 119
    assert result[1][2] == 99

    assert result[2][0] == 254
    assert result[2][1] == 219
    assert result[2][2] == 199
