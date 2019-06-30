from power_method import dominant_eigen_system


class TestEigenSystem:
    def test_dominant_eigen_system(self):
        matrix = [[7, -2, 0], [-2, 6, -2], [0, -2, 5]]

        result = dominant_eigen_system(matrix)

        assert result == 43
