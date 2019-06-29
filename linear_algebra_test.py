import pytest
from linear_algebra import matrix_multiply, norm, matrix_scalar_multiply

class TestNorm:
    def test_norm_row_vector(self):
        a = [1, 2, 2]
        result = norm(a)
        assert result == 3

    def test_norm_column_vector(self):
        a = [[1], [2], [2]]
        result = norm(a)
        assert result == 3

    def test_fail_empty_vector(self):
        with pytest.raises(ValueError):
            norm([])

    def test_fail_non_column_or_row(self):
        with pytest.raises(ValueError):
            norm([[2, 3], [4, 5]])


class TestMatrixMultiply:
    def test_multiply(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[1, 5], [1, 2], [1, 1]]

        result = matrix_multiply(a, b)

        assert result == [[6, 12], [15, 36], [24, 60]]


    def test_fail_incompatible_dimensions(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        b = [[1, 5, 3], [1, 2, 3]]

        with pytest.raises(ValueError):
            matrix_multiply(a, b)

class TestMatrixScalarMultiply:
    def test_multiply_3_by_3_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

        result = matrix_scalar_multiply(matrix, 2)

        assert matrix == [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Ensure the input is unchanged
        assert result == [[2, 4, 6], [8, 10, 12], [14, 16, 18]] 

    def test_multiply_row_vector(self):
        result = matrix_scalar_multiply([1, 2, 3], 2)

        assert result == [2, 4, 6]

    def test_fail_empty_vector(self):
        with pytest.raises(ValueError):
           matrix_scalar_multiply([], 2)