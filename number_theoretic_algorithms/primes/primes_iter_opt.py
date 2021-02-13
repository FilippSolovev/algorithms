"""Count prime numbers in a range between 1 and a given number.

Count prime numbers with an opimized iterative algorithm by reducing number
of inner loops (shift the upper limit of loop counts from a number itself to
the square root of the number and jumping through odd numbers while looping)

Usage
-----

    $ python3 primes_iter_opt.py num

num - an upper limit for a range to look for prime numbers in.
"""

from math import sqrt
import sys


def is_prime(num):
    """Checks if the number is prime."""
    if num == 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    limit = int(sqrt(num)) + 1
    for i in range(3, limit, 2):
        if num % i == 0:
            return False
    return True


def get_primes_count(num):
    """Iteratively counts prime numbers in a range between 1 and num."""
    count = sum(1 if is_prime(i) else 0 for i in range(2, num + 1))
    return count


def main():
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        sys.exit()

    output = get_primes_count(num)
    print(output)


if __name__ == '__main__':
    main()

    # unit tests for is_prime
    # assert not is_prime(1)
    # assert is_prime(3)
    # assert not is_prime(8)

    # unit tests for get_primes_count
    # assert get_primes_count(1) == 0
    # assert get_primes_count(10) == 4
    # assert get_primes_count(100) == 25
