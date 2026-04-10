import math

from sorts import *


def __introsort(arr, left, right, depth):
    if depth == 0:
        se_heapsort(arr, left, right + 1)

    if right <= left:
        return

    pivot = right
    i = left

    for j in range(left, right):
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[pivot] = arr[pivot], arr[i]

    __introsort(arr, left, i - 1, depth - 1)
    __introsort(arr, i + 1, right, depth - 1)


def introsort(arr):
    max_depth = int(2 * math.log2(len(arr))) if len(arr) > 0 else 0
    __introsort(arr, 0, len(arr) - 1, max_depth)


if __name__ == '__main__':
    arr = [6, 5, 8, 7, 1, 0, 10, 9, 3, 2]
    print(arr)
    introsort(arr)
    print(arr)
