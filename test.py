from sorts import introsort
from sorts.counter_classes.Counter import Counter
from random import shuffle

import sorts.counter_classes.CountingInsertionSort as Insort
import sorts.counter_classes.CountingHeapsort as Heapsort
import sorts.counter_classes.CountingIntrosort as Introsort
import sorts.counter_classes.CountingQsort as Qsort

import time
import sys

sys.setrecursionlimit(100000)

data = list(range(1, 10000))
shuffle(data)

introsort_counter = Counter()
qsort_counter = Counter()

introsort_sort = Introsort.CountingIntrosort(introsort_counter)
qsort_sort = Qsort.CountingQsort(qsort_counter)


start = time.perf_counter()

introsort_sort.introsort(data.copy())
qsort_sort.qsort(data.copy())

time_1 = time.perf_counter() - start


print(qsort_counter.get_counter(), introsort_counter.get_counter())
