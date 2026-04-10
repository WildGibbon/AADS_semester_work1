def __qsort(arr, left, right):  # тута мы включаем концы
    if right <= left:
        return

    pivot = right
    i = left

    for j in range(left, right):
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[pivot] = arr[pivot], arr[i]

    __qsort(arr, left, i - 1)
    __qsort(arr, i + 1, right)


def qsort(arr):
    __qsort(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    arr = [6, 5, 8, 7, 1, 0, 10, 9, 3, 2]
    __qsort(arr, 0, len(arr) - 1)
    print(arr)
