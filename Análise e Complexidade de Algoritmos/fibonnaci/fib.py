import time
import functools as ft


def cache(f):
    d = {}
    def fib(idx):
        if idx in d:
            return d[idx]
        else:
            r = f(idx)
            d[idx] = r
            return r
    return fib

#@ft.cache
def fib(idx):
    if idx <= 1:
        return idx

    return fib(idx-1) + fib(idx-2)



def fibVetor(idx):
    if idx <= 1:
        return idx
    v = [0]*(idx+1)
    v[0] = 0
    v[1] = 1
    for i in range(2, idx+1):
        v[i] = v[i-1] + v[i-2]
    return v[idx]

def fibVariaveis(idx):
    if idx <= 1:
        return idx
    p = 0
    u = 1
    r = 0
    for _ in range(idx-1):
        r = p + u
        p = u
        u = r
    return r


for i in range(50):
    ti = time.process_time()
    print(i, fib(i), time.process_time() - ti)

    ti = time.process_time()
    print(i, fibVetor(i), time.process_time() - ti)

    ti = time.process_time()
    print(i, fibVariaveis(i), time.process_time() - ti)

