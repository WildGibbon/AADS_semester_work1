from random import randint


def insertion_sort(arr, start, end):
    for i in range(start, end):
        key = arr[i]
        j = i - 1

        while j >= start and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == '__main__':
    arr = [randint(0, 10) for i in range(10)]
    print(arr)
    insertion_sort(arr, 5, len(arr))
    print(arr)
