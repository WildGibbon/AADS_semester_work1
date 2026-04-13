from sorts.counter_classes.Counter import Counter

import sorts.counter_classes.CountingIntrosort as Introsort
import sorts.counter_classes.CountingQsort as Qsort
import dataframe_image as dfimage
import pandas as pd
import sys


sys.setrecursionlimit(100000)

qsort_counter = Counter()
introsort_counter = Counter()
introsort_sort = Introsort.CountingIntrosort(introsort_counter)
qsort_sort = Qsort.CountingQsort(qsort_counter)

counts_1 = []
counts_2 = []
lengths = []

data_path = "../data_generation/data.txt"
data = []

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

df = pd.DataFrame()
df['length'] = lengths
df['introsort'] = counts_1
df['qsort'] = counts_2

dfimage.export(df, "../results/qsort_introsort_cnt.png", dpi=300)

