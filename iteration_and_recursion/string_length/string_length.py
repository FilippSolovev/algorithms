import sys


def len_iter(input_string):
    """Iterative function to get length of given string."""
    length = 0
    for _ in input_string:
        length += 1
    return length


def len_recur(input_string):
    """Recursive function to get length of given string."""
    if input_string == '':
        return 0
    else:
        return 1 + len_recur(input_string[1:])


if __name__ == '__main__':

    opts = [opt for opt in sys.argv[1:] if opt.startswith('-')]
    args = [arg for arg in sys.argv[1:] if not arg.startswith('-')]

    if not len(args):
        sys.exit()

    if '-i' in opts:
        print(len_iter(''.join(args)))
    elif '-r' in opts:
        print(len_recur(''.join(args)))
    else:
        print(len(''.join(args)))
