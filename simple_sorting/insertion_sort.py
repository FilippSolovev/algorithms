import sys
from helper import read_data


# def insertion_sort(array):
#     array_length = len(array)
#     for i in range(1, array_length):
#         elem = array[i]
#         j = i - 1
#         while (j >= 0 and array[j] > elem):
#             array[j + 1] = array[j]
#             j -= 1
#         array[j + 1] = elem
#     return array

def insertion_sort(array):
    # more pythonic
    array_length = len(array)
    for i in range(1, array_length):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
    return array


def main():

    # args = sys.argv[1:]
    #
    # if not len(args):
    #     sys.exit()
    #
    # array = [*map(cast_to_numeric, args)]
    # output = insertion_sort(array)
    # print(' '.join(str(elem) for elem in output))

    file_name = sys.argv[1]
    if not len(file_name):
        sys.exit()

    array = read_data(file_name)

    output = insertion_sort(array)
    print(' '.join(str(elem) for elem in output))


if __name__ == '__main__':
    main()
