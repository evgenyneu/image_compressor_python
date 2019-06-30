import pytest
from linear_algebra import matrix_multiply, norm, matrix_scalar_multiply, \
    matrix_size, transpose, dot_product, gramian, matrix_add


class TestGramian:
    def test_gramian(self):
        matrix = [[3, -2], [-3, 2]]

        result = gramian(matrix)

        assert result == [[18, -12], [-12, 8]]


class TestDotProduct:
    def test_dot_product(self):
        vector1 = [[1], [4], [7]]
        vector2 = [[2], [5], [8]]

        result = dot_product(vector1, vector2)

        assert result == 78


class TestTranspose:
    def test_transpose(self):
        matrix = [[1, 2], [4, 5], [7, 8]]
        result = transpose(matrix)
        assert result == [[1, 4, 7], [2, 5, 8]]


class TestNorm:
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


class TestMatrixAdd:
    def test_matrix_add(self):
        a = [[1, 2, 3], [4, 5, 6]]
        b = [[-2, 0, 1], [7, -2, 13]]

        result = matrix_add(a, b)

        assert result == [[-1, 2, 4], [11, 3, 19]]


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

        assert matrix == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Ensure the input is unchanged
        assert result == [[2, 4, 6], [8, 10, 12], [14, 16, 18]]


class TestMatrixSize:
    def test_matrix(self):
        matrix = [[1, 2], [4, 5], [7, 8]]
        rows, columns = matrix_size(matrix)

        assert rows == 3
        assert columns == 2

    def test_row_vector2(self):
        matrix = [[1, 2, 3]]
        rows, columns = matrix_size(matrix)

        assert rows == 1
        assert columns == 3

    def test_column_vector(self):
        matrix = [[1], [2], [3]]
        rows, columns = matrix_size(matrix)

        assert rows == 3
        assert columns == 1

    def test_empty(self):
        matrix = []
        rows, columns = matrix_size(matrix)

        assert rows == 0
        assert columns == 0
