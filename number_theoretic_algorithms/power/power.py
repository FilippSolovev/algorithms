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


if __name__ == '__main__':
    a = power_iter(1.000001, 100)
    print(a)

    b = power_by_squaring(1.000001, 100)
    print(b)

    c = power_binary_expansion(1.000001, 100)
    print(c)
