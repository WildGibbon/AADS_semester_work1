from abc import ABC


class ICounting(ABC):
    def get_counter(self):
        pass

    def reset_counter(self):
        pass
