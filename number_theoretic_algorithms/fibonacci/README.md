# Fibonacci number

Different algorithms to find the [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) in a sequence.

# Example

The scripts can be run like any other Python scripts - type `python` followed by a script name and a term number in the Fibonacci sequence, like:

~~~
$ python fib_iter.py 10
~~~

To run tests with the [naive-tester](https://github.com/FilippSolovev/naive-tester) (it should be installed first) use the following command:

~~~
$ tester fib_matrix.py tests
~~~

You can also run tests for all four algorithms in the cloud by clicking on [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FilippSolovev/algorithms/blob/master/number_theoretic_algorithms/fibonacci/fibonacci_test_report.ipynb)

# Algorithms comparison

The execution times for all scripts are presented in the table below.

| Input arguments | 0 | 1 | 2 | 3 | 4 | 5 | 10 | 100 | 1000 | 10000 | 100000 | 1000000 | 10000000 |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Recursive | 0.04s | 0.05s | 0.04s | 0.04s | 0.04s | 0.05s | 0.04s | x | x | x | x | x | x |
| Iterative| 0.05s | 0.05s | 0.05s | 0.04s | 0.05s | 0.04s | 0.07s | 0.07s | 0.05s | 0.05s | 0.24s | 14.57s | 1799.96s |
| Golden ratio| 0.05s | 0.05s | 0.05s | 0.05s | 0.07s | 0.05s | 0.06s | 0.06s | 0.05s | 0.05s (x) | 0.14s (x) | 0.22s (x) | x |
| Product of matrices| 0.06s | 0.05s | 0.05s | 0.05s | 0.05s | 0.04s | 0.07s | 0.06s | 0.05s | 0.06s | 0.84s | 92.64s | 5219.77s |
