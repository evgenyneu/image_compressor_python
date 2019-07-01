from power_method import dominant_eigen_system
from pytest import approx
import numpy as np


class TestDominantEigenSystem:
    def test_dominant_eigen_system(self):
        matrix = np.array([[7, -2, 0], [-2, 6, -2], [0, -2, 5]])

        eigenvalue, eigenvector = dominant_eigen_system(matrix, 4)

        assert eigenvalue == approx(8.887124, rel=1e-5)
        assert len(eigenvector) == 3
        assert eigenvector[0][0] == approx(0.785224, rel=1e-5)
        assert eigenvector[1][0] == approx(-0.585385, rel=1e-5)
        assert eigenvector[2][0] == approx(0.201857, rel=1e-5)

    def test_zero_matrix(self):
        matrix = [[0, 0], [0, 0]]

        eigenvalue, eigenvector = dominant_eigen_system(matrix, 4)

        assert eigenvalue == 0
        assert len(eigenvector) == 0
