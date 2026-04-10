import time
from random import randint

import sorts


a = [randint(0, 10000000) for i in range(1000000)]

start = time.time()
sorts.heapsort(a)
print(time.time() - start)

start = time.time()
sorts.qsort(a)
print(time.time() - start)