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
    if exp == 0:
        return 1

    result = 1
    for _ in range(exp):
        result *= num
    return result


def power_2n(num, exp):
    """Binary exponentiation.

    The function to compute exponentiation by powers of two with
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


def power_binary_exp(num, exp):
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


if __name__ == '__main__':
    a = power_iter(3, 100)
    print(a)

    b = power_2n(3, 100)
    print(b)

    c = power_binary_exp(3, 100)
    print(c)
