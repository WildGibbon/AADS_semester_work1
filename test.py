import random
import time

from sorts import introsort, qsort


def quicksort_fast(arr, left, right):
    if right <= left:
        return

    # Случайный pivot
    pivot_idx = random.randint(left, right)
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]

    pivot = right
    i = left

    for j in range(left, right):
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[pivot] = arr[pivot], arr[i]

    quicksort_fast(arr, left, i - 1)
    quicksort_fast(arr, i + 1, right)


# Тест
data = list(range(1000000))  # Отсортированный массив - worst case для вашего кода
random.shuffle(data)  # Перемешаем для теста

start = time.time()
qsort(data)
print(f"Время: {time.time() - start:.3f} сек")