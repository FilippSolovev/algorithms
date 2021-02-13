"""Calculate the Fibonacci number using the Golden Ratio.

Usage
-----

    $ python3 fib_golden_ratio.py num

num - a term number in the Fibonacci sequence.
"""


from math import sqrt
import sys


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


def main():
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        sys.exit()

    output = fibonacci_golden_ratio(num)
    print(output)


if __name__ == '__main__':
    main()

    # unit tests
    # assert fibonacci_golden_ratio(0) == 0
    # assert fibonacci_golden_ratio(1) == 1
    # assert fibonacci_golden_ratio(2) == 1
    # assert fibonacci_golden_ratio(3) == 2
    # assert fibonacci_golden_ratio(4) == 3
    # assert fibonacci_golden_ratio(5) == 5
