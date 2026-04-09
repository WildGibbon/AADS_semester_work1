def qsort(arr, left, right):
    if len(arr[left:right + 1]) <= 1:
        return arr

    pivot = right
    i = left

    for j in range(left, right):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[pivot] = arr[pivot], arr[i]

    qsort(arr, left, i-1)
    qsort(arr, i+1, right)

    return arr


if __name__ == '__main__':
    arr = [5, 1, 3, 2, 45, 7, 3, 10, 4]
    a = qsort(arr, 0, len(arr) - 1)
    print(a)

