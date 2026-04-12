from sorts.counter_classes.ICounter import ICounter


class Counter(ICounter):
    def __init__(self):
        self.__counter = 0

    def increase_counter(self):
        self.__counter += 1

    def reset_counter(self):
        self.__counter = 0

    def get_counter(self):
        return self.__counter

