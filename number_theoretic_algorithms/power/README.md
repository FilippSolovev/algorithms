# Exponentiation algorithms

Here is a couple of algorithms to quickly raise a number to the integer power and their comparison with the basic iterative algorithm.

# Example

The scripts can be run like any other Python scripts - type `python` followed by a script name and two parameters: a number to be raised to some power and an exponent. For example to compute 2<sup>10</sup> iteratively type:

~~~
$ python power_iter.py 2 10
~~~

To run tests with the [naive-tester](https://github.com/FilippSolovev/naive-tester) (it should be installed first) use the following command:
~~~
$ tester power_by_squaring.py tests
~~~

You can also run tests for all three algorithms in the cloud by clicking on [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FilippSolovev/algorithms/blob/master/number_theoretic_algorithms/power/power_test_report.ipynb)

# Algorithms comparison

The execution times for all scripts are presented in the table below.

| Input arguments | 2<sup>10</sup> | 123456789<sup>0</sup> | 1.001<sup>1000</sup> | 1.0001<sup>10000</sup> | 1.00001<sup>100000</sup> | 1.000001<sup>1000000</sup> | 1.0000001<sup>10000000</sup> | 1.00000001<sup>100000000</sup> | 1.000000001<sup>1000000000</sup> | 1.0000000001<sup>10000000000</sup> |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Iterative| 0.06s | 0.06s | 0.05s | 0.08s | 0.07s | 0.10s | 0.55s | 4.63s | 45.43s | 455.33s |
| Exponentiating by squaring| 0.06s | 0.05s | 0.05s | 0.05s | 0.05s | 0.07s | 0.12s | 1.55s | 21.28s | 65.68s |
| Exponent binary expansion| 0.05s | 0.05s | 0.05s | 0.05s | 0.05s | 0.04s | 0.05s | 0.05s | 0.04s | 0.05s |
