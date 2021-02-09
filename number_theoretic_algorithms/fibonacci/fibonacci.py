from copy import deepcopy
from math import sqrt


def fibonacci_iterative(num):
    """The Fibonacci number.

    Calculate the Fibonacci number iteratively.

    Parameters
    ----------
        num: int
            a term number.

    Returns
    -------
        int
            a Fibonacci number for a given term number.
    """
    previous, current = 0, 1
    for _ in range(num):
        previous, current = current, previous + current
    return previous


def fibonacci_golden_ratio(num):
    """The Fibonacci number.

    Calculate the Fibonacci number using the Golden Ratio.

    Parameters
    ----------
        num: int
            a term number.

    Returns
    -------
        int
            a Fibonacci number for a given term number.
    """
    phi = (sqrt(5) + 1) / 2
    return int(phi**num / sqrt(5) + 0.5)


def matrix_product(mtrx_a, mtrx_b):
    """Product of two 2x2 matrices."""
    # output_00 = mtrx_a[0][0] * mtrx_b[0][0] + mtrx_a[0][1] * mtrx_b[1][0]
    # output_01 = mtrx_a[0][0] * mtrx_b[0][1] + mtrx_a[0][1] * mtrx_b[1][1]
    # output_10 = mtrx_a[1][0] * mtrx_b[0][0] + mtrx_a[1][1] * mtrx_b[1][0]
    # output_11 = mtrx_a[1][0] * mtrx_b[0][1] + mtrx_a[1][1] * mtx_b[1][1]
    output = [[mtrx_a[0][0] * mtrx_b[0][0] + mtrx_a[0][1] * mtrx_b[1][0],
               mtrx_a[0][0] * mtrx_b[0][1] + mtrx_a[0][1] * mtrx_b[1][1]],
              [mtrx_a[1][0] * mtrx_b[0][0] + mtrx_a[1][1] * mtrx_b[1][0],
               mtrx_a[1][0] * mtrx_b[0][1] + mtrx_a[1][1] * mtrx_b[1][1]]]
    return output


def matrix_exp(mtrx, exp):
    """Exponentiation of a 2x2 matrix."""
    if exp == 0:
        return [[1, 0], [0, 1]]

    iter_num = len(bin(exp)[2:])
    result = deepcopy(mtrx)
    power_of_2 = 1

    for _ in range(1, iter_num):
        result = matrix_product(result, result)
        power_of_2 *= 2

    for _ in range(power_of_2, exp):
        result = matrix_product(result, mtrx)

    return result


def fibonacci_through_matrices(num):
    """The Fibonacci number.

    Calculate the Fibonacci number using product of matrices.

    Parameters
    ----------
        number: int
            a term number.

    Returns
    -------
        int
            a Fibonacci number for a given term number.
    """
    if num == 0:
        return 0

    if num == 1:
        return 1

    fib_initial = [[1, 1], [1, 0]]
    fib_matrix = matrix_exp(fib_initial, num - 1)
    return fib_matrix[0][0]


if __name__ == '__main__':
    assert fibonacci_iterative(7) == 13
    assert fibonacci_iterative(15) == 610

    assert fibonacci_golden_ratio(7) == 13
    assert fibonacci_golden_ratio(15) == 610

    assert fibonacci_through_matrices(7) == 13
    assert fibonacci_through_matrices(15) == 610
