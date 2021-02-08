def fibonacci_iterative(number):
    """The Fibonacci number.

    Calculate the Fibonacci number iteratively.

    Parameters
    ----------
        number: int
            a term number.

    Returns
    -------
        int
            a Fibonacci number for a given term number.
    """
    previous, current = 0, 1
    for _ in range(number):
        previous, current = current, previous + current
    return previous


def fibonacci_golden_ratio():
    """The Fibonacci number.

    Calculate the Fibonacci number using the Golden Ratio.

    Parameters
    ----------
        number: int
            a term number.

    Returns
    -------
        int
            a Fibonacci number for a given term number.
    """
    pass


def fibonacci_through_matrices():
    """The Fibonacci number.

    Calculate the Fibonacci number using product of matrices.

    Parameters
    ----------
        number: int
            a term number.

    Returns
    -------
        int
            a Fibonacci number for a given term number.
    """
    pass


if __name__ == '__main__':
    assert fibonacci_iterative(7) == 13
    assert fibonacci_iterative(15) == 610
