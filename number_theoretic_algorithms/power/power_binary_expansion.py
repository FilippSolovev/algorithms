"""Raise the number to the power of exp.

Usage
-----

    $ python3 power_binary_expansion.py num exp

num - a number, the base for the exponentiation
exp - an exponent, the power.
"""

import sys


def power_binary_expansion(num, exp):
    """Exponentiation by binary expansion of the exponent.

    The function to compute exponentiation by converting the exponent to base2.

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
    inter_result = num
    power_of_2 = 1
    deg_exp = exp
    while power_of_2 * 2 < exp:
        power_of_2 *= 2
        deg_exp = deg_exp // 2
        inter_result *= inter_result
        result *= inter_result if deg_exp % 2 else 1

    return result


def main():
    if len(sys.argv) > 2:
        num = float(sys.argv[1])
        exp = int(sys.argv[2])
    else:
        sys.exit()

    output = float(power_binary_expansion(num, exp))
    print(output)


if __name__ == '__main__':
    main()

    # unit tests
    # assert power_binary_expansion(2, 10) == 1024.0
    # assert power_binary_expansion(123456789, 0) == 1.0
