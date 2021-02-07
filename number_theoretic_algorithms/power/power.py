def power_iter(num, exp):
    """Iterative exponentiation.

    The function to compute exponentiation iteratively

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

    result = 1
    for _ in range(exp):
        result *= num
    return result


def power_2n():
    """Binary exponentiation.

    The function to compute exponentiation by powers of two with multiplication.

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


def power_binary_exp():
    """Binary exponentiation.

    The function to compute exponentiation by converion the power to base-2.

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

    pass


if __name__ == '__main__':
    # a = power_iter(2, 4)
    # print(a)

    a = 100
    b = str(bin(a))[2:]
    print(b)
