"""Calculate the Fibonacci number iteratively.

Usage
-----

    $ python3 fib_iter.py num

num - a term number in the Fibonacci sequence.
"""

import sys


def fibonacci_iter(num):
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


def main():
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        sys.exit()

    output = fibonacci_iter(num)
    print(output)


if __name__ == '__main__':
    main()

    # unit tests
    # assert fibonacci_iter(0) == 0
    # assert fibonacci_iter(1) == 1
    # assert fibonacci_iter(2) == 1
    # assert fibonacci_iter(3) == 2
    # assert fibonacci_iter(4) == 3
    # assert fibonacci_iter(5) == 5
