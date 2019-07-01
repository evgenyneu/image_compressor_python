from power_method import dominant_eigen_system, svd, singular_value_expansion
from pytest import approx


class TestDominantEigenSystem:
    def test_dominant_eigen_system(self):
        matrix = [[7, -2, 0], [-2, 6, -2], [0, -2, 5]]

        eigenvalue, eigenvector = dominant_eigen_system(matrix, 4)

        assert eigenvalue == approx(8.887124, rel=1e-5)
        assert len(eigenvector) == 3
        assert eigenvector[0][0] == approx(0.785224, rel=1e-5)
        assert eigenvector[1][0] == approx(-0.585385, rel=1e-5)
        assert eigenvector[2][0] == approx(0.201857, rel=1e-5)


class TestSVD:
    def test_svd(self):
        matrix = [[2, -1], [-1, 2]]

        result = svd(matrix, max_eigenvalues=2, iterations=10)

        assert len(result) == 2

        assert result[0][0] == [[0.7071067812541464], [-0.7071067811189488]]
        assert result[0][1] == 2.9999999999999996
        assert result[0][2] == [[0.7071067813893437], [-0.7071067809837512]]

        assert result[1][0] == [[0.7071067805781589], [0.7071067817949361]]
        assert result[1][1] == 0.9999999999999998
        assert result[1][2] == [[0.7071067809837509], [0.707106781389344]]


class TestSingularValueExpansion:
    def test_singular_value_expansion(self):
        svd_data = [
            (
                [[0.7071067812541464], [-0.7071067811189488]],
                2.9999999999999996,
                [[0.7071067813893437], [-0.7071067809837512]]
             ),
            (
                [[0.7071067805781589], [0.7071067817949361]],
                0.9999999999999998, [[0.7071067809837509],
                [0.707106781389344]]
            )
        ]

        result = singular_value_expansion(svd_data)

        assert result == [
                [1.9999999999999996, -0.9999999999999998],
                [-0.9999999999999999, 1.9999999999999996]
            ]
