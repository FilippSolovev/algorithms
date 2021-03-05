import sys
from helper import read_data


def selection_sort(array):
    array_length = len(array)
    for i in range(array_length - 1):
        min_index = i
        for j in range(i + 1, array_length):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array


def main():

    # args = sys.argv[1:]
    #
    # if not len(args):
    #     sys.exit()
    #
    # array = [*map(cast_to_numeric, args)]

    file_name = sys.argv[1]
    if not len(file_name):
        sys.exit()

    array = read_data(file_name)

    output = selection_sort(array)
    print(' '.join(str(elem) for elem in output))


if __name__ == '__main__':
    main()
