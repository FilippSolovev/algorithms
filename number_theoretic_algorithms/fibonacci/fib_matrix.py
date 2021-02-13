"""Calculate the Fibonacci number using multiplication of matrices.

Usage
-----

    $ python3 fib_matrix.py num

num - a term number in the Fibonacci sequence.
"""

from copy import deepcopy
import sys


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


def fibonacci_matrix_form(num):
    """The Fibonacci number.

    Calculate the Fibonacci number using a product of matrices.

    Parameters
    ----------
        num: int
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


def main():
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        sys.exit()

    output = fibonacci_matrix_form(num)
    print(output)


if __name__ == '__main__':
    main()

    # unit tests
    # assert fibonacci_matrix_form(0) == 0
    # assert fibonacci_matrix_form(1) == 1
    # assert fibonacci_matrix_form(2) == 1
    # assert fibonacci_matrix_form(3) == 2
    # assert fibonacci_matrix_form(4) == 3
    # assert fibonacci_matrix_form(5) == 5
