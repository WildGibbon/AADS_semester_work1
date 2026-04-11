from cmath import log

from scipy.ndimage import label

from sorts import *
import time
import sys
import matplotlib.pyplot

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

matplotlib.pyplot.plot(lengths, [i*log(i, 2)*0.000000065 for i in lengths], label="nlogn")
matplotlib.pyplot.plot(lengths, times_1, label="introsort")
matplotlib.pyplot.plot(lengths, times_2, label="qsort")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
