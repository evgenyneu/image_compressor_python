from core import load_image, compress_image, iterations_for_terms, compression_ratio, \
    dir_filename_extension, compress_image_to_file, compressed_image_path

import os
from pytest import approx


class TestCompressImageToFile:
    def test_compress_image_to_file(test):
        path = "images/for_compression/marmite_100x100.jpg"
        result = compress_image_to_file(path, terms=10)
        output_path = result['output_path']
        assert output_path == 'images/for_compression/marmite_100x100_10_terms_5.0x_compression.jpg'
        assert os.path.exists(output_path)
        os.remove(output_path)

    def test_compress_image_to_file_specify_path(test):
        path = "images/for_compression/marmite_100x100.jpg"
        path_out = "images/for_compression/marmite_100x100_test.jpg"
        result = compress_image_to_file(path, path_out=path_out, terms=10)
        output_path = result['output_path']
        assert output_path == path_out
        assert os.path.exists(output_path)
        os.remove(output_path)


class TestCompressImage:
    def test_compress_image(self):
        data = load_image("images/for_compression/marmite_100x100.jpg")
        # width, height = image_size(data)
        # path_out = compressed_image_path(path, width=width, height=height, terms=10)
        result = compress_image(data, terms=10)

        assert result['compressed_data'].shape == (100, 100, 3)
        assert result['iterations'] == 10
        # assert os.path.exists(path_out)
        # os.remove(path_out)

    def test_compress_image_supply_iterations(self):
        data = load_image("images/for_compression/marmite_100x100.jpg")

        result = compress_image(data, terms=10, iterations=7)

        assert result['compressed_data'].shape == (100, 100, 3)
        assert result['iterations'] == 7


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
