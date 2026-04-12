from sorts.counter_classes.ICounter import ICounter


class CountingHeapsort:
    def __init__(self, counter: ICounter):
        self.counter = counter

    def heapsort(self, arr, start, end):
        for root in range((end - start) // 2, start - 1, -1):
            self.counter.increase_counter()

            self.__heapify(arr, root, end)

        for i in range(end, start, -1):
            self.counter.increase_counter()

            arr[start], arr[i - 1] = arr[i - 1], arr[start]
            self.__heapify(arr, start, i - 1)

    def __heapify(self, arr, root, end):
        self.counter.increase_counter()

        left = 2 * root + 1
        right = 2 * root + 2
        largest = root

        if left < end and arr[left] > arr[largest]:
            largest = left

        if right < end and arr[right] > arr[largest]:
            largest = right

        if largest != root:
            arr[root], arr[largest] = arr[largest], arr[root]
            self.__heapify(arr, largest, end)
