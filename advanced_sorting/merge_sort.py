from copy import deepcopy


def bottom_up_merge(left, right):
    merged = []
    while True:
        if not left:
            break
        if not right:
            break

        if left[0] < right[0]:
            left_head = left.pop(0)
            # print('left head:{}'.format(left_head))
            # print('l:{}'.format(left))
            merged.append(left_head)
            # print('resulting:{}'.format(merged))
        else:
            right_head = right.pop(0)
            # print('right head:{}'.format(right_head))
            # print('r:{}'.format(right))
            merged.append(right_head)
            # print('resulting:{}'.format(merged))

    while True:
        if not left:
            break
        left_head = left.pop(0)
        merged.append(left_head)

    while True:
        if not right:
            break
        right_head = right.pop(0)
        merged.append(right_head)
    return merged


def bottom_up_merge_sort(array):
    array_length = len(array)
    width = 1
    while width < array_length:
        tmp_array = []
        i = 0
        while i < array_length:
            left = array[i:min(i + width, array_length)]
            right = array[min(i + width, array_length):
                          min(i + 2 * width, array_length)]
            tmp_array += bottom_up_merge(left, right)
            i = i + 2 * width
        array = deepcopy(tmp_array)
        width *= 2
    return array


if __name__ == '__main__':
    # test_array = [121, 33, 23423, 0, -23, 100, 99, -999, 1]
    test_array = [81, 94, 11, 96, 12, 35, 17, 99, 28, 58, 41, 75, 15]
    print(' '.join(str(elem) for elem in test_array))
    array = bottom_up_merge_sort(test_array)
    print(' '.join(str(elem) for elem in array))
