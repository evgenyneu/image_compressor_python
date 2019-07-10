from core import load_image, compress_image, iterations_for_terms, compression_ratio, \
    dir_filename_extension, compress_image_to_file, compressed_image_path

import os
from pytest import approx


class TestCompressImageToFile:
    def test_compress_image_to_file_specify_path(self):
        path = "images/for_compression/marmite_100x100.jpg"
        path_out = "images/for_compression/marmite_100x100_test.jpg"
        result = compress_image_to_file(path, path_out=path_out, terms=10, annotate=True)
        output_path = result['output_path']
        assert output_path == path_out
        assert os.path.exists(output_path)
        os.remove(output_path)

    def test_compress_image_to_file(self):
        path = "images/for_compression/marmite_100x100.jpg"
        result = compress_image_to_file(path, terms=10, annotate=True)
        output_path = result['output_path']
        assert output_path == 'images/for_compression/marmite_100x100_10_terms_5.0x_compression.jpg'
        assert os.path.exists(output_path)
        assert result['compression_ratio'] == 5
        os.remove(output_path)

    def test_compress_image_to_file_3_by_3(self):
        path = "images/test_3x3.bmp"
        path_out = "images/test_3x3_output.bmp"

        result = compress_image_to_file(path, path_out=path_out, terms=1, iterations=1,
                                        annotate=False)

        output_path = result['output_path']
        assert output_path == path_out
        assert os.path.exists(output_path)
        os.remove(output_path)


class TestCompressImage:
    def test_compress_image(self):
        data = load_image("images/for_compression/marmite_100x100.jpg")
        result = compress_image(data, terms=10)

        assert result['compressed_data'].shape == (100, 100, 3)
        assert result['iterations'] == 10

    def test_compress_image_supply_iterations(self):
        data = load_image("images/for_compression/marmite_100x100.jpg")

        result = compress_image(data, terms=10, iterations=7)

        assert result['compressed_data'].shape == (100, 100, 3)
        assert result['iterations'] == 7

    def test_compress_image_that_crashed(self):
        data = load_image("images/none_type_test.png")

        result = compress_image(data, terms=3)

        assert result['compressed_data'].shape == (256, 302, 3)


class TestCompressImagePath:
    def test_compressed_image_path(self):
        path = "/dir/images/marmite_750x375.jpg"
        result = compressed_image_path(path, width=750, height=150, terms=8)

        assert result == "/dir/images/marmite_750x375_8_terms_15.6x_compression.jpg"

    def test_compressed_image_path_filename_without_dir(self):
        path = "marmite_750x375.jpg"
        result = compressed_image_path(path, width=750, height=150, terms=8)

        assert result == "marmite_750x375_8_terms_15.6x_compression.jpg"


class TestDirFilenameExtension:
    def test_dir_filename_extension(self):
        path = "/dir/dir2/my.cat.jpg"
        dirname, filename_without_extension, file_extension = dir_filename_extension(path)

        assert dirname == "/dir/dir2"
        assert filename_without_extension == "my.cat"
        assert file_extension == ".jpg"

    def test_dir_filename_extension_filename_without_dir(self):
        path = "my.cat.jpg"
        dirname, filename_without_extension, file_extension = dir_filename_extension(path)

        assert dirname == ""
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


def test_load_image_four_chanels():
    result = load_image('images/test_3x3.bmp')
    assert result.shape == (3, 3, 3)

    red = result[:, :, 0]
    assert red[0][0] == 80
    assert red[0][1] == 60
    assert red[0][2] == 0

    assert red[1][0] == 150
    assert red[1][1] == 120
    assert red[1][2] == 100

    assert red[2][0] == 255
    assert red[2][1] == 220
    assert red[2][2] == 200

    green = result[:, :, 1]
    assert green[0][0] == 85
    assert green[0][1] == 65
    assert green[0][2] == 5

    assert green[1][0] == 155
    assert green[1][1] == 125
    assert green[1][2] == 105

    assert green[2][0] == 255
    assert green[2][1] == 225
    assert green[2][2] == 205

    blue = result[:, :, 2]
    assert blue[0][0] == 90
    assert blue[0][1] == 70
    assert blue[0][2] == 10

    assert blue[1][0] == 160
    assert blue[1][1] == 130
    assert blue[1][2] == 110

    assert blue[2][0] == 255
    assert blue[2][1] == 230
    assert blue[2][2] == 210
