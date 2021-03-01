import sys
from helper import read_data


def cast_to_numeric(string):
    if string.find('.') == -1:
        return int(string)
    return float(string)


def heapify(array, root, size):
    left_index = 2 * root + 1
    right_index = left_index + 1
    top_index = root
    if (left_index < size) and (array[top_index] < array[left_index]):
        top_index = left_index
    if (right_index < size) and (array[top_index] < array[right_index]):
        top_index = right_index
    if top_index == root:
        return array
    array[top_index], array[root] = array[root], array[top_index]
    heapify(array, top_index, size)


def heap_sort(array):
    for i in range(len(array) // 2 - 1, -1, -1):
        heapify(array, i, len(array))
    for j in range(len(array) - 1, 0, -1):
        array[0], array[j] = array[j], array[0]
        heapify(array, 0, j)
    return array


def main():

    # args = sys.argv[1:]
    #
    # if not len(args):
    #     sys.exit()
    #
    # array = [*map(cast_to_numeric, args)]
    # output = heap_sort(array)
    # print(output)

    file_name = sys.argv[1]
    if not len(file_name):
        sys.exit()

    array = read_data(file_name)

    output = heap_sort(array)
    print(' '.join(str(elem) for elem in output))


if __name__ == '__main__':
    main()
