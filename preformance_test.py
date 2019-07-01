from linear_algebra import norm
from random import randint
from timeit import default_timer
import numpy as np


def test_matrix_multiply_performance():
    size = 500
    # a = [[randint(0, 100) for _ in range(1)] for i in range(size)]
    # b = [[randint(0, 100) for _ in range(1)] for i in range(size)]

    # start = default_timer()
    # result_one = norm(a)
    # end = default_timer()

    # print(f"Duration (one): {end - start} s")

    # a = np.array(a)
    # b = np.array(b)

    # start = default_timer()
    # result_two = norm_two(a)
    # end = default_timer()

    # print(f"Duration (two): {end - start} s")

    # assert result_one == result_two

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

