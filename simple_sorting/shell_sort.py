import sys
from helper import read_data


def shell_sort(array):
    array_length = len(array)

    # 1: Shell, 1959
    gaps = [array_length // 2**k for k in range(array_length)]
    gaps = [gap for gap in gaps if gap > 0]

    # 2: Ciura, 2001
    # gaps_init = [701, 301, 132, 57, 23, 10, 4, 1]
    # gaps = [gap for gap in gaps_init if gap <= array_length]

    # 3: Papernov and Stasevich, 1965
    # gaps = [(2**k + 1) for k in range(array_length)][::-1]
    # gaps = gaps + [1]

    for gap in gaps:
        # for i in range(gap, array_length):
        #     elem = array[i]
        #     j = i
        #     while (j >= gap and array[j - gap] > elem):
        #         array[j] = array[j - gap]
        #         j -= gap
        #     array[j] = elem
        # same as above, but more pythonic:
        for i in range(gap, array_length):
            for j in range(i, 0, -1 * gap):
                if array[j - gap] > array[j]:
                    array[j - gap], array[j] = array[j], array[j - gap]
    return array


def main():

    # args = sys.argv[1:]
    #
    # if not len(args):
    #     sys.exit()
    #
    # array = [*map(cast_to_numeric, args)]
    # output = shell_sort(array)
    # print(output)

    file_name = sys.argv[1]
    if not len(file_name):
        sys.exit()

    array = read_data(file_name)

    output = shell_sort(array)
    print(' '.join(str(elem) for elem in output))


if __name__ == '__main__':
    main()
