import numpy as np


def BubbleSort(v):
    n = len(v)
    for i in range(n-1):
        for j in range(n-1):
            if v[j] > v[j+1]:
                t = v[j]
                v[j] = v[j+1]
                v[j+1] = t
    return v

v = np.random.randint(1, 1000, 10)

BubbleSort(v)
print(v)
