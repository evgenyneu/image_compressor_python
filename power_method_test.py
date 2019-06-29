from power_method import eigen_system
import pytest

class TestEigenSystem:
    @pytest.mark.skip(reason="Unimplemented")
    def test_eigen_system(self):
        matrix = [[3, -2], [-3, 2]]
        
        result = eigen_system(matrix, 2)

        assert result == 42
