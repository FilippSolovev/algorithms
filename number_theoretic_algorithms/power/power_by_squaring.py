"""Raise the number to the power of exp.

Usage
-----

    $ python3 power_by_squaring.py num exp

num - a number, the base for the exponentiation
exp - an exponent, the power.
"""

import sys


def power_by_squaring(num, exp):
    """Exponentiation by square and multiply.

    The function to compute exponentiation by squaring with residiual
    multiplication.

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

    result = num
    power_of_2 = 1
    while power_of_2 * 2 < exp:
        power_of_2 *= 2
        result *= result

    for _ in range(power_of_2, exp):
        result *= num

    return result


def main():
    if len(sys.argv) > 2:
        num = float(sys.argv[1])
        exp = int(sys.argv[2])
    else:
        sys.exit()

    output = float(power_by_squaring(num, exp))
    print(output)


if __name__ == '__main__':
    main()

    # unit tests
    # assert power_by_squaring(2, 10) == 1024.0
    # assert power_by_squaring(123456789, 0) == 1.0
