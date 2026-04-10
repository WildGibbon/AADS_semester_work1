from random import randint


def __heapify(arr, root, end):
    left = 2 * root + 1
    right = 2 * root + 2
    largest = root

    if left < end and arr[left] > arr[largest]:
        largest = left

    if right < end and arr[right] > arr[largest]:
        largest = right

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        __heapify(arr, largest, end)


def heapsort(arr):
    for root in range(len(arr) // 2 - 1, -1, -1):
        __heapify(arr, root, len(arr))

    for end in range(len(arr), 0, -1):
        arr[0], arr[end - 1] = arr[end - 1], arr[0]
        __heapify(arr, 0, end - 1)


def se_heapsort(arr, start, end):
    for root in range((end - start) // 2, start - 1, -1):
        __heapify(arr, root, end)

    for i in range(end, start, -1):
        arr[0], arr[i - 1] = arr[i - 1], arr[0]
        __heapify(arr, 0, i - 1)


if __name__ == '__main__':
    arr = [6, 5, 8, 7, 1, 0, 10, 9, 3, 2]
    se_heapsort(arr, 0, 10)
    print(arr)

