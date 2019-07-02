from linear_algebra import matrix_size, dot_product, gramian


class TestGramian:
    def test_gramian(self):
        matrix = [[3, -2], [-3, 2]]

        result = gramian(matrix)

        assert result.tolist() == [[18, -12], [-12, 8]]


class TestDotProduct:
    def test_dot_product(self):
        vector1 = [[1], [4], [7]]
        vector2 = [[2], [5], [8]]

        result = dot_product(vector1, vector2)

        assert result == 78


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
