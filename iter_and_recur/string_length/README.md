# String Length

Two basic ways to compute the length of a string: iterative and recursive. Dive into the code to see their implementations. An option `-r` is for calling a recursive function whereas `-i` will run an iterative one. Without options the script engages a standard python `len` function.

# Example

To get the number of characters in a string 'abcdefg' recursively simply type  
~~~~
$ python string_length.py -r abcdefg
~~~~
or iteratively
~~~~
$ python string_length.py -i abcdefg
~~~~

To run the tests in the `tests` folder first install the [naive-tester](https://github.com/FilippSolovev/naive-tester) (it's better to do this in a virtual environment):
~~~~
$ pip install naive-tester
~~~~
then to run tests type:
~~~~
$ tester string_length.py tests
~~~~
