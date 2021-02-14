"""Count prime numbers with the seive of Eratosthenes.

The optimized algorithm with O(n) complexity is used.

Usage
-----

    $ python3 eratosthenes_linear.py num

num - an upper limit for a range to look for prime numbers in.
"""

import sys


def eratosthenes_linear(num):
    """The sieve of Eratosthenes with O(n) complexity."""
    sieve = [0] * (num + 1)
    primes = []
    count = 0
    for i in range(2, num + 1):
        if sieve[i] == 0:
            sieve[i] = i
            primes.append(i)
            count += 1
        for pr in primes:
            if pr <= sieve[i] and pr * i <= num:
                sieve[pr * i] = pr
            else:
                break
    return count


def main():
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        sys.exit()

    output = eratosthenes_linear(num)
    print(output)


if __name__ == '__main__':
    main()

    # unit tests
    # assert eratosthenes_linear(1) == 0
    # assert eratosthenes_linear(10) == 4
    # assert eratosthenes_linear(100) == 25
