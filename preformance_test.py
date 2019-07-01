from linear_algebra import matrix_scalar_multiply
from random import randint
from timeit import default_timer
import numpy as np


def test_matrix_multiply_performance():
    size = 500
    a = [[randint(0, 100) for _ in range(size)] for i in range(size)]
    # b = [[randint(0, 100) for _ in range(size)] for i in range(size)]

    # start = default_timer()
    # result_one = matrix_scalar_multiply(a, 2.3123)
    # end = default_timer()

    # print(f"Duration (one): {end - start} s")

    # a = np.array(a)

    # start = default_timer()
    # result_two = matrix_scalar_multiply_two(a, 2.3123)
    # end = default_timer()

    # print(f"Duration (two): {end - start} s")

    # assert result_one == result_two.tolist()

    # start = default_timer()
    # result_two = matrix_multiply_two(a, b)
    # end = default_timer()

    # print(f"Duration (one): {end - start} s")

    # start = default_timer()
    # result_three = matrix_multiply_three(a, b)
    # end = default_timer()

    # print(f"Duration (one): {end - start} s")

    # assert result_one == result_two
    # assert result_two == result_three.tolist()

