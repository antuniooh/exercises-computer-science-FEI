import random
import time

def digito(num, dig):
    for _ in range(dig):
        num = int(num / 10)
    return num % 10


def countingSortEst(v, d):
    count = [0] * 10
    temp = list(v)
    for el in range(len(v)):
        count[digito(el, d)] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for el in reversed(v):
        temp[count[digito(el, d)] - 1] = el
        count[digito(el, d)] -= 1
    return temp

def radix(v):
  d = 10
  for i in range(d):
    v = countingSortEst(v, i)
  return v


v = [123, 434, 255, 656, 744, 888]


for i in range(10):
  n =i*100
  vetor = [random.randint(0,9999) for _ in range(n)]
  inicio = time.process_time_ns()
  radix(vetor)
  dt = time.process_time_ns() - inicio 
  print(n, dt)
