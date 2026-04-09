from random import randint
import sys

sys.setrecursionlimit(10000)


def heapify(arr, root, end):
    left = 2 * root + 1
    right = 2 * root + 2
    largest = root

    if left < end and arr[left] > arr[largest]:
        largest = left

    if right < end and arr[right] > arr[largest]:
        largest = right

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, largest, end)


def heapsort(arr):
    for root in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, root, len(arr))

    for end in range(len(arr), 0, -1):
        arr[0], arr[end - 1] = arr[end - 1], arr[0]
        heapify(arr, 0, end - 1)


if __name__ == '__main__':
    arr = [randint(0, 10000) for i in range(1000000)]
    sorted(arr)
    print("aga")

# TODO доделать heapsort
