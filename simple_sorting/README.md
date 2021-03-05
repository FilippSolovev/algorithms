# Sorting algorithms

Various sorting algorithms: [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort), [selection sort](https://en.wikipedia.org/wiki/Selection_sort), [Shell sort](https://en.wikipedia.org/wiki/Shellsort) and [heapsort](https://en.wikipedia.org/wiki/Heapsort).

# Example

The scripts can be run like any other Python scripts - type `python` followed by a script name and name of the file containing the array to sort.

~~~
$ python heap_sort.py tests/random/test_1.txt
~~~

To run tests with the [naive-tester](https://github.com/FilippSolovev/naive-tester) (it should be installed first) use the following command (here we have four sets of tests, so the name to the specific folder should be specified):

~~~
$ tester heap_sort.py tests/random
~~~

You can also run tests for all four sorting algorithms in the cloud by clicking on []()

# Sorting algorithms comparison

The execution times for all scripts are presented in the table below.

| Algorithm  | Array Type | 1 | 10 | 100 | 1000 | 10000 | 100000 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Insertion sort | Random digits | 0.04s | 0.04s | 0.04s | 0.11s | 8.10s | 802.95s |
| Selection sort | Random digits | 0.04s | 0.04s | 0.04s | 0.08s | 3.82s | 379.50s |
| Shell sort, 1959 | Random digits | 0.04s | 0.04s | 0.04s | 0.12s | 9.55s | 817.71s |
| Heap sort | Random digits | 0.04s | 0.04s | 0.04s | 0.04s | 0.10s | 0.75s |
| Insertion sort | Random numbers | 0.04s | 0.04s | 0.04s | 0.11s | 8.07s | 902.92s |
| Selection sort | Random numbers | 0.04s | 0.04s | 0.04s | 0.07s | 3.70s | 403.93s |
| Shell sort, 1959 | Random numbers | 0.04s | 0.04s | 0.04s | 0.12s | 9.73s | 988.39s |
| Heap sort | Random numbers | 0.04s | 0.04s | 0.04s | 0.04s | 0.10s | 0.86s |
| Insertion sort | Sorted | 0.04s | 0.05s | 0.04s | 0.08s | 5.03s | 504.98s |
| Selection sort | Sorted | 0.04s | 0.04s | 0.04s | 0.08s | 3.81s | 380.67s |
| Shell sort, 1959 | Sorted | 0.04s | 0.04s | 0.04s | 0.12s | 10.00s | 863.74s |
| Heap sort | Sorted |  Sorted | 0.04s | 0.04s | 0.04s | 0.05s | 0.11s | 0.88s |
| Insertion sort | Reversely sorted | 0.04s | 0.04s | 0.04s | 0.14s | 11.11s | 1147.10s |
| Selection sort | Reversely sorted | 0.04s | 0.05s | 0.04s | 0.07s | 3.72s | 381.60s |
| Shell sort, 1959 | Reversely sorted | 0.04s | 0.04s | 0.04s | 0.11s | 9.73s | 837.60s |
| Heap sort | Reversely sorted | 0.04s | 0.04s | 0.04s | 0.04s | 0.10s | 0.81s |

Clear winner here is the Heap sort algorithm and it's not a surprise, since its complexity is O(n log n) while others have O(n<sup>2</sup>).
