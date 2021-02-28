import sys


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
    for i in range(len(array) // 2 - 1, 0, -1):
        heapify(array, 0, len(array))
    for j in range(len(array) - 1, 0, -1):
        array[0], array[j] = array[j], array[0]
        heapify(array, 0, j)
    return array


def main():
    # test_array = [112, 6.22, 5, 0.12, -3, -2.0008, 1, 1.011]
    # print(heap_sort(test_array))

    args = sys.argv[1:]

    if not len(args):
        sys.exit()

    array = [*map(cast_to_numeric, args)]
    output = heap_sort(array)
    print(output)


if __name__ == '__main__':
    main()
