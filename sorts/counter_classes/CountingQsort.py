from sorts.counter_classes.ICounter import ICounter


class CountingQsort:
    def __init__(self, counter: ICounter):
        self.__counter = counter

    def __qsort(self, arr, left, right):
        self.__counter.increase_counter()

        if right <= left:
            return

        pivot = right
        i = left

        for j in range(left, right):
            self.__counter.increase_counter()

            if arr[j] < arr[pivot]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[pivot] = arr[pivot], arr[i]

        self.__qsort(arr, left, i - 1)
        self.__qsort(arr, i + 1, right)

    def qsort(self, arr):
        self.__qsort(arr, 0, len(arr) - 1)
