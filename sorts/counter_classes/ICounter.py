from abc import ABC


class ICounter(ABC):
    def get_counter(self):
        pass

    def increase_counter(self):
        pass

    def reset_counter(self):
        pass
