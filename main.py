from sorts import *
import time
import sys
import matplotlib.pyplot

sys.setrecursionlimit(10000)


data_path = "data_generation/data.txt"
data = []
times = []


with open(data_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        data.append(list(map(int, line.split())))


for i in range(0, len(data)):
    start = time.time()
    introsort(data[i])
    times.append((time.time() - start))

matplotlib.pyplot.plot(times)
matplotlib.pyplot.show()
