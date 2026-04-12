from sorts.counter_classes.ICounter import ICounter


class CountingInsertionSort:
    def __init__(self, counter: ICounter):
        self.__counter = counter

    def insertion_sort(self, arr, start, end):
        for i in range(start, end):
            self.__counter.increase_counter()

            key = arr[i]
            j = i - 1

            while j >= start and key < arr[j]:
                self.__counter.increase_counter()

                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key
