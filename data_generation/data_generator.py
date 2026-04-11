from random import randint


class arr_random_generator:
    def __init__(self, upper_limit, lower_limit, count, save_path):
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit
        self.count = count
        self.save_path = save_path

        if count > (upper_limit - lower_limit):
            raise ValueError('Thats wrong bro')

    def execute(self):
        with open(self.save_path, "w") as f:
            if self.count == 1:
                for i in range(self.upper_limit + 1):
                    f.write(str(randint(0, 10000)) + " ")

                return

            step = (self.upper_limit - self.lower_limit) // (self.count - 1)

            for length in range(self.lower_limit, self.upper_limit + 1, step):
                for i in range(length):
                    f.write(str(randint(0, 10000)) + " ")
                f.write("\n")


if __name__ == "__main__":
    generator = arr_random_generator(50000, 100, 100, "data.txt")
    generator.execute()

