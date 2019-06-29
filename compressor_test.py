import pytest
from compressor import load_image, matrix_multiply


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
