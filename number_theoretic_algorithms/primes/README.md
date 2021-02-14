# Prime numbers

Computation methods to find all prime numbers up to any given limit. To be precise insted of finding prime numbers themselves the aggregate of them - count - is being sought. Two kinds of algorithms are examined - the trial division (iterative) with its modifications and the [sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).

# Example

The scripts can be run like any other Python scripts - type `python` followed by a script name and a limit within which the prime numbers should be counted, like:

~~~
$ python primes_iter.py 100
~~~

To run tests with the [naive-tester](https://github.com/FilippSolovev/naive-tester) (it should be installed first) use the following command:

~~~
$ tester eratosthenes.py tests
~~~

You can also run tests for all five algorithms in the cloud by clicking on [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FilippSolovev/algorithms/blob/master/number_theoretic_algorithms/primes/primes_test_report.ipynb)

# Algorithms comparison

The execution times for all scripts are presented in the table below.

| Input arguments | 10 | 1 | 2 | 3 | 4 | 5 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000 | 100000000 | 1000000000 | 123456789 |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Iterative| 0.04s | 0.05s | 0.04s | 0.04s | 0.05s | 0.05s | 0.05s | 0.05s | 0.42s | 29.55s | x | x | x | x | x |
| Iterative optimized| 0.04s | 0.05s | 0.04s | 0.04s | 0.05s | 0.04s | 0.05s | 0.05s | 0.05s | 0.15s | 2.54s | 62.38s | x | x | x |
| Iterative memo| 0.03s | 0.03s | 0.05s | 0.05s | 0.04s | 0.03s | 0.03s | 0.03s | 0.04s | 0.17s | 2.60s | 51.31s | x | x | 1624.08s |
| Eratosthenes| 0.03s | 0.03s | 0.04s | 0.04s | 0.04s | 0.04s | 0.04s | 0.05s | 0.04s | 0.06s | 0.21s | 1.92s | 20.67s | 237.33s | 26.01s |
| Eratosthenes O(n)| 0.04s | 0.05s | 0.04s | 0.04s | 0.04s | 0.04s | 0.04s | 0.04s | 0.04s | 0.08s | 0.37s | 3.49s | 34.02s | 347.33s | 42.58s | 