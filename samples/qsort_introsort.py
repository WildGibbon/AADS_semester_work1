from cmath import log
from sorts import *

import matplotlib.pyplot as plt
import time
import sys

sys.setrecursionlimit(10000)


data_path = "data_generation/data.txt"
data = []
times_1 = []
times_2 = []
times_3 = []
lengths = []


with open(data_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        arr = list(map(int, line.split()))
        data.append(arr)


for i in range(0, len(data)):
    start = time.perf_counter()
    introsort(data[i].copy())
    time_1 = time.perf_counter() - start

    start = time.perf_counter()
    qsort(data[i].copy())
    time_2 = time.perf_counter() - start

    print(i)

    times_1.append(time_1)
    times_2.append(time_2)
    lengths.append(len(data[i]))

plt.plot(lengths, [i*log(i, 2)*0.000000065 for i in lengths], label="nlogn(*65*10^-7)")
plt.plot(lengths, times_1, label="introsort")
plt.plot(lengths, times_2, label="qsort")
plt.legend()
plt.show()
