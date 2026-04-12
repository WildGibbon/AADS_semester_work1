from sorts.counter_classes.Counter import Counter
from cmath import log

import sorts.counter_classes.CountingIntrosort as Introsort
import sorts.counter_classes.CountingQsort as Qsort
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)

introsort_counter = Counter()
qsort_counter = Counter()

introsort_sort = Introsort.CountingIntrosort(introsort_counter)
qsort_sort = Qsort.CountingQsort(qsort_counter)

data_path = "data.txt"
data = []
counts_1 = []
counts_2 = []
lengths = []


with open(data_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        arr = list(map(int, line.split()))
        data.append(arr)


for i in range(0, len(data)):
    introsort_counter.reset_counter()
    qsort_counter.reset_counter()

    introsort_sort.introsort(data[i].copy())
    qsort_sort.qsort(data[i].copy())

    counts_1.append(introsort_counter.get_counter())
    counts_2.append(qsort_counter.get_counter())
    lengths.append(len(data[i]))


plt.plot(lengths, [i*log(i, 2)*1.27 for i in lengths], label="nlogn")
plt.plot(lengths, counts_1, label="introsort")
plt.plot(lengths, counts_2, label="qsort")
plt.legend()
plt.show()