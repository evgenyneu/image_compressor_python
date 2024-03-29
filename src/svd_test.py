from svd import find_u_from_v, svd, singular_value_expansion
import math
from pytest import approx
import numpy as np
from numpy.testing import assert_allclose


class TestVectorU:
    def test_find_u_from_v(self):
        matrix = np.array([[3, -2], [-3, 2]])
        eigenvalue = 25.999999999999996
        singular_value = math.sqrt(eigenvalue)
        eigenvector = np.array([[0.8320502943378436], [-0.5547001962252291]])

        result = find_u_from_v(matrix, v=eigenvector, singular_value=singular_value)

        assert len(result) == 2
        assert result[0][0] == approx(0.707106, rel=1e-5)
        assert result[1][0] == approx(-0.707106, rel=1e-5)


class TestSVD:
    def test_svd(self):
        matrix = np.array([[2, -1], [-1, 2]])

        result = svd(matrix, max_eigenvalues=2, iterations=10)

        assert len(result) == 2

        assert_allclose(result[0][0], [[0.7071067812541463], [-0.7071067811189488]])
        assert result[0][1] == approx(3)
        assert_allclose(result[0][2], [[0.7071067813893437], [-0.7071067809837513]])

        assert_allclose(result[1][0], [[0.7071067805781592], [0.7071067817949359]])
        assert result[1][1] == approx(1)
        assert_allclose(result[1][2], [[0.7071067809837512], [0.7071067813893438]])

    def test_svd_with_zero_singular_values(self):
        matrix = [[3, -2], [-3, 2]]

        result = svd(matrix, max_eigenvalues=2, iterations=10)

        assert len(result) == 1

        assert_allclose(result[0][0], [[0.7071067811865475], [-0.7071067811865475]])
        assert result[0][1] == approx(5.099019513592785)
        assert_allclose(result[0][2], [[0.8320502943378437], [-0.5547001962252291]])


class TestSingularValueExpansion:
    def test_singular_value_expansion(self):
        svd_data = [
            (
                np.array([[0.7071067812541464], [-0.7071067811189488]]),
                2.9999999999999996,
                np.array([[0.7071067813893437], [-0.7071067809837512]])
             ),
            (
                np.array([[0.7071067805781589], [0.7071067817949361]]),
                0.9999999999999998,
                np.array([[0.7071067809837509], [0.707106781389344]])
            )
        ]

        result = singular_value_expansion(svd_data)

        assert_allclose(result, [
                [1.9999999999999996, -0.9999999999999998],
                [-0.9999999999999999, 1.9999999999999996]
            ])

    def test_singular_value_expansion_zero_singular_value(self):
        svd_data = [
            (
                np.array([[0.7071067811865476], [-0.7071067811865476]]),
                5.0990195135927845,
                np.array([[0.8320502943378436], [-0.5547001962252291]])
            )
        ]

        result = singular_value_expansion(svd_data)

        assert_allclose(result, [[3, -2], [-3, 2]])
