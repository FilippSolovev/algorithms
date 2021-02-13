"""Count prime numbers in a range between 1 and a given number.

Count prime numbers with an iterative algorithm optimized by storing found
primes in a dictionary.

Usage
-----

    $ python3 primes_memo.py num

num - an upper limit for a range to look for prime numbers in.
"""

from math import sqrt
import sys


primes = {}  # a global dict to store prime numbers


def is_prime(num):
    """Checks if the number is prime."""
    if num == 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    limit = int(sqrt(num)) + 1
    for i in range(1, limit):
        try:
            if primes[i] > limit:
                break
            if num % primes[i] == 0:
                return False
        except KeyError:
            break
    return True


def get_primes_count(num):
    """Iteratively counts prime numbers in a range between 1 and num."""
    if num == 1:
        return 0

    count = 0
    primes[0] = 2

    for i in range(3, num + 1, 2):
        if is_prime(i):
            count += 1
            primes[count] = i
    return count + 1


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
