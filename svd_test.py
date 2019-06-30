from svd import find_u_from_v
import math
from pytest import approx


class TestVectorU:
    def test_find_u_from_v(self):
        matrix = [[3, -2], [-3, 2]]
        eigenvalue = 25.999999999999996
        singular_value = math.sqrt(eigenvalue)
        eigenvector = [[0.8320502943378436], [-0.5547001962252291]]

        result = find_u_from_v(matrix, v=eigenvector, singular_value=singular_value)

        assert len(result) == 2
        assert result[0][0] == approx(0.707106, rel=1e-5)
        assert result[1][0] == approx(-0.707106, rel=1e-5)
