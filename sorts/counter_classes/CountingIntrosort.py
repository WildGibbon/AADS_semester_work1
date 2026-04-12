import math

from sorts.counter_classes.CountingHeapsort import CountingHeapsort
from sorts.counter_classes.CountingInsertionSort import CountingInsertionSort
from sorts.counter_classes.ICounter import ICounter


class CountingIntrosort:
    def __init__(self, counter: ICounter):
        self.__counter = counter
        self.heapsort = CountingHeapsort(counter)
        self.insort = CountingInsertionSort(counter)

    def introsort(self, arr):
        max_depth = int(2 * math.log2(len(arr))) if len(arr) > 0 else 0
        self.__introsort(arr, 0, len(arr) - 1, max_depth)

    def __introsort(self, arr, left, right, depth):
        self.__counter.increase_counter()

        if right <= left:
            return

        if depth == 0:
            self.heapsort.heapsort(arr, left, right + 1)
            return

        if right - left < 16:
            self.insort.insertion_sort(arr, left, right + 1)
            return

        pivot = right
        i = left

        for j in range(left, right):
            self.__counter.increase_counter()

            if arr[j] < arr[pivot]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[pivot] = arr[pivot], arr[i]

        self.__introsort(arr, left, i - 1, depth - 1)
        self.__introsort(arr, i + 1, right, depth - 1)
