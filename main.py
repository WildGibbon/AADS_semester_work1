from sorts import *

import pandas as pd
import sys
import time

sys.setrecursionlimit(10000)


data_path = "samples/data.txt"
data = []
times_1 = []
times_2 = []
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

df = pd.DataFrame()
df['lengths'] = lengths
df['introsort'] = times_1
df['qsort'] = times_2

with open("results/times_table.xlsx", "wb") as f:
    df.to_excel(f, index=False)


