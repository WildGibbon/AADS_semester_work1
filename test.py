from sorts.counter_classes.Counter import Counter
from random import shuffle

import sorts.counter_classes.CountingInsertionSort as Insort
import time
import sys

sys.setrecursionlimit(100000)

counter = Counter()
data = list(range(1, 1000))
shuffle(data)

start = time.perf_counter()

sort = Insort.CountingInsertionSort(counter)
sort.insertion_sort(data, 0, len(data) - 1)

time_1 = time.perf_counter() - start

print(time_1, counter.get_counter())
