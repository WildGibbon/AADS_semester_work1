from sorts.counter_classes.ICounting import ICounting


class CountingInsertionSort(ICounting):
    def __init__(self):
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def reset_counter(self):
        self.__counter = 0

    def insertion_sort(self, arr, start, end):
        for i in range(start, end):
            self.__counter += 1

            key = arr[i]
            j = i - 1

            while j >= start and key < arr[j]:
                self.__counter += 1

                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key
