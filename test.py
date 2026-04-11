import time
from random import shuffle

from sorts import *
import sys
sys.setrecursionlimit(100000)


data = list(range(1, 10000))

start = time.perf_counter()
qsort(data)
time_1 = time.perf_counter() - start

print(time_1)
