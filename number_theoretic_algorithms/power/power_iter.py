"""Raise the number to the power of exp.

Usage
-----

    $ python3 power_iter.py num exp

num - a number, the base for the exponentiation
exp - an exponent, the power.
"""

import sys


def power_iter(num, exp):
    """Iterative exponentiation.

    The function to compute exponentiation iteratively.

    Parameters
    ----------
        num: float
            base, a positive real number.
        exp: int
            power, a positive integer (exp >= 0).

    Returns
    -------
        numeric
            the expth power of num.

    """
    if exp == 0:
        return 1

    result = 1
    for _ in range(exp):
        result *= num
    return result


def main():
    if len(sys.argv) > 2:
        num = float(sys.argv[1])
        exp = int(sys.argv[2])
    else:
        sys.exit()

    output = float(power_iter(num, exp))
    print(output)


if __name__ == '__main__':
    main()

    # unit tests
    # assert power_iter(2, 10) == 1024.0
    # assert power_iter(123456789, 0) == 1.0
