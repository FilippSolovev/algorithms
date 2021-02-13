"""Count prime numbers with the seive of Eratosthenes.

Usage
-----

    $ python3 eratosthenes.py num

num - an upper limit for a range to look for prime numbers in.
"""

import sys


def eratosthenes(num):
    """The sieve of Eratosthenes for counting prime numbers in a range."""
    sieve = [True] * (num + 1)
    count = 0
    for i in range(2, num + 1):
        if sieve[i]:
            count += 1
            for j in range(i * i, num + 1, i):
                sieve[j] = False
    return count


def main():
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        sys.exit()

    output = eratosthenes(num)
    print(output)


if __name__ == '__main__':
    main()

    # unit tests
    # assert eratosthenes(1) == 0
    # assert eratosthenes(10) == 4
    # assert eratosthenes(100) == 25
