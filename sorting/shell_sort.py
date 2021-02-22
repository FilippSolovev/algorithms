import sys


def insertion_sort(array):
    # more pythonic
    array_length = len(array)
    for i in range(1, array_length):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
    return array


def shell_sort(array):
    array_length = len(array)
    # 1:
    # gaps_init = [701, 301, 132, 57, 23, 10, 4, 1]
    # gaps = [gap for gap in gaps_init if gap <= array_length]

    # 2:
    # gaps = [array_length // 2**k for k in range(array_length)]

    # 3:
    gaps = [(2**k + 1) for k in range(array_length)][::-1]
    for gap in gaps:
        # for i in range(gap, array_length):
        #     elem = array[i]
        #     j = i
        #     while (j >= gap and array[j - gap] > elem):
        #         array[j] = array[j - gap]
        #         j -= gap
        #     array[j] = elem
        for i in range(gap, array_length):
            for j in range(i, 0, -1 * gap):
                if array[j - gap] > array[j]:
                    array[j - gap], array[j] = array[j], array[j - gap]
    return array


def main():

    args = sys.argv[1:]

    if not len(args):
        sys.exit()

    array = [*map(cast_to_numeric, args)]
    output = shell_sort(array)
    print(output)


if __name__ == '__main__':
    # main()
    test_array = [2, 0, -15, -29, -1, 0, 99, 3.002, -0.000012]
    # test_array = [2, 0, -15, -29, -1, 0]
    print(test_array)
    print(shell_sort(test_array))
