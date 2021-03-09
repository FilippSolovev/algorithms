from copy import deepcopy


def merge_sort(array):
    if len(array) > 1:
        middle_point = len(array)//2
        left = array[:middle_point]
        right = array[middle_point:]

        merge_sort(left)
        merge_sort(right)
        array = merge(array, left, right)

        return array


def merge(array, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return array


# def merge_sort(array):
#     # doesn't work properly
#     if len(array) > 1:
#         middle_point = len(array)//2
#
#         left = array[:middle_point]
#         right = array[middle_point:]
#
#         merge_sort(left)
#         merge_sort(right)
#         array = merge(left, right)
#
#         return array
#
#
# def merge(left, right):
#     # doesn't work properly
#     array = []
#
#     while len(left) > 0 and len(right) > 0:
#         if left[0] <= right[0]:
#             array.append(left.pop(0))
#         else:
#             array.append(right.pop(0))
#
#     # Checking if any element was left
#     while len(left) > 0:
#         array.append(left.pop(0))
#
#     while len(right) > 0:
#         array.append(right.pop(0))
#
#     return array


def copy_array(source_array, target_array, n):
    for i in range(n):
        target_array[i] = source_array[i]


def bottom_up_merge(array, i_left, i_right, i_end, tmp_array):

    i, j = i_left, i_right
    for k in range(i_left, i_end):
        if i < i_right and (j >= i_end or array[i] <= array[j]):
            tmp_array[k] = array[i]
            i += 1
        else:
            tmp_array[k] = array[j]
            j += 1


def bottom_up_merge_sort(array, n):
    tmp_array = deepcopy(array)
    k = 1
    for width in range(1, n, 2 * k):
        k = width
        l = 0
        for i in range(0, n, l + 2 * width):
            l = i + 1
            bottom_up_merge(array,
                            i,
                            min(i + width, n),
                            min(i + 2 * width, n),
                            tmp_array)
        copy_array(tmp_array, array, n)
    return array


if __name__ == '__main__':
    test_array = [121, 33, 23423, 0, -23, 100, 99, -999]
    print(' '.join(str(elem) for elem in test_array))
    array = merge_sort(test_array)
    print(' '.join(str(elem) for elem in array))
    array = bottom_up_merge_sort(test_array, len(test_array))
    # print(array)
    print(' '.join(str(elem) for elem in array))
