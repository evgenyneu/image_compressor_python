from linear_algebra import matrix_multiply, matrix_multiply_two, matrix_multiply_three
from random import randint
from timeit import default_timer


def test_matrix_multiply_performance():
    size = 200
    a = [[randint(0, 100) for _ in range(size)] for i in range(size)]
    b = [[randint(0, 100) for _ in range(size)] for i in range(size)]

    start = default_timer()
    result_one = matrix_multiply(a, b)
    end = default_timer()

    print(f"Duration (one): {end - start} s")

    start = default_timer()
    result_two = matrix_multiply_two(a, b)
    end = default_timer()

    print(f"Duration (one): {end - start} s")

    start = default_timer()
    result_three = matrix_multiply_three(a, b)
    end = default_timer()

    print(f"Duration (one): {end - start} s")

    assert result_one == result_two
    assert result_two == result_three.tolist()

