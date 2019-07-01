from compressor import load_image, compress_image, iterations_for_terms, compression_ratio
import os
import pytest
from pytest import approx


def test_compress_image():
    path_out = f"images/marmite_750x375_test.bmp"
    compress_image("images/marmite_750x375.jpg", path_out, terms=10)
    assert os.path.exists(path_out)
    os.remove(path_out)


@pytest.mark.skip(reason="Long test that creates images at different resolutions")
def test_compress_image_color():
    for size in [[100, 100], [500, 500], [750, 375], [1000, 1000]]:
        width = size[0]
        height = size[1]
        size_test = f"{width}x{height}"

        for terms in [1, 2, 5, 10, 20, 50, 100, 150, 200, 300, 500]:
            out_dir = f"images/{size_test}"

            if not os.path.exists(out_dir):
                os.makedirs(out_dir)

            ratio = compression_ratio(width=width, height=height, terms=terms)

            if ratio > 1.2:
                continue

            compression = f"{(1/ratio):0.1f}x_compression"
            path_out = f"{out_dir}/marmite_{size_test}_compressed_{terms}_terms_{compression}.jpg"
            compress_image(f"images/marmite_{size_test}.jpg", path_out, terms=terms)
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
