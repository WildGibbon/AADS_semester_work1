from random import shuffle

from sorts import *

import sys
import time
import sorts.counter_classes.CountingInsertionSort as insertionsort

sys.setrecursionlimit(100000)

data = list(range(1, 1000))
shuffle(data)

start = time.perf_counter()
sort = insertionsort.CountingInsertionSort()

sort.insertion_sort(data, 0, len(data) - 1)
time_1 = time.perf_counter() - start

print(time_1, sort.get_counter())
