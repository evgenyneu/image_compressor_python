from compressor import load_image, matrix_multiply
import pytest


def test_matrix_multiply():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[1, 5], [1, 2], [1, 1]]

    result = matrix_multiply(a, b)

    assert result == [[6, 12], [15, 36], [24, 60]]


def test_matrix_multiply_incompatible_dimensions():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[1, 5, 3], [1, 2, 3]]

    with pytest.raises(ValueError):
        matrix_multiply(a, b)


def test_load_image():
    result = load_image('marmite_500x500_gray.bmp')
    assert result.shape == (500, 500)
