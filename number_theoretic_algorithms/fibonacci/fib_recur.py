"""Calculate the Fibonacci number recursively.

Usage
-----

    $ python3 fib_iter.py num

num - a term number in the Fibonacci sequence.
"""

import sys


def fibonacci_recur(num):
    """The Fibonacci number.

    Calculate the Fibonacci number recursively.

    Parameters
    ----------
        num: int
            a term number.

    Returns
    -------
        int
            a Fibonacci number for a given term number.
    """
    if num > 1:
        return fibonacci_recur(num - 1) + fibonacci_recur(num - 2)
    else:
        return num


def main():
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        sys.exit()

    output = fibonacci_recur(num)
    print(output)


if __name__ == '__main__':
    main()

    # unit tests
    # assert fibonacci_recur(0) == 0
    # assert fibonacci_recur(1) == 1
    # assert fibonacci_recur(2) == 1
    # assert fibonacci_recur(3) == 2
    # assert fibonacci_recur(4) == 3
    # assert fibonacci_recur(5) == 5
