"""Count prime numbers in a range between 1 and a given number iteratively.

Usage
-----

    $ python3 primes_iter.py num

num - an upper limit for a range to look for prime numbers in.
"""

import sys


def is_prime(num):
    """Checks if the number is prime."""
    if num == 1:
        return False

    for i in range(2, num):
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
