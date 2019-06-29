import pytest
from compressor import load_image, matrix_multiply, norm


class TestNorm:
    def test_norm_row_vector(self):
        a = [1, 2, 2]
        result = norm(a)
        assert result == 3

    def test_norm_column_vector(self):
        a = [[1], [2], [2]]
        result = norm(a)
        print(type(result))
        assert result == 3

    def test_fail_empty_vector(self):
        with pytest.raises(ValueError):
            norm([])

    def test_fail_non_column_or_row(self):
        with pytest.raises(ValueError):
            norm([[2, 3], [4, 5]])


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
