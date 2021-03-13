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
            merged.append(left_head)
        else:
            right_head = right.pop(0)
            merged.append(right_head)

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


# def bottom_up_merge_sort(array):
#     """Bottom up merge sort with the usage of 4 arrays as buffers."""
#     array_length = len(array)
#     tape_a = array[: array_length // 2]
#     tape_b = array[array_length // 2:]
#     tape_idx = 0
#     width = 1
#     while width < array_length:
#         tape_c = []
#         tape_d = []
#         tmp_array = [tape_c, tape_d]
#         i = 0
#         for i in range(0, array_length, width):
#             left = tape_a[i:min(i + width, array_length)]
#             right = tape_b[i:min(i + width, array_length)]
#             tmp_array[tape_idx] += bottom_up_merge(left, right)
#             tape_idx = 1 - tape_idx
#         tape_a = deepcopy(tape_c)
#         tape_b = deepcopy(tape_d)
#         width *= 2
#     output = [tape_a, tape_b]
#     return output[tape_idx]


if __name__ == '__main__':
    # test_array = [121, 33, 23423, 0, -23, 100, 99, -999, 1]
    test_array = [81, 94, 11, 96, 12, 35, 17, 99, 28, 58, 41, 75, 15]
    print(' '.join(str(elem) for elem in test_array))
    array = bottom_up_merge_sort(test_array)
    print(' '.join(str(elem) for elem in array))
