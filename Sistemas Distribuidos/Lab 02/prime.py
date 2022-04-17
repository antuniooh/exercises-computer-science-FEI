import sympy
import concurrent.futures
import psutil

def check_prime(data):
    prime = 0
    for i in range(len(data)):
        if sympy.isprime(data[i]):
            prime += 1
    return prime

def is_prime(data):
    tamanholista = len(data)
    primos = 0
    for i in range(tamanholista):
        if sympy.isprime(data[i]):
            primos += 1
    return primos

def is_prime_thread(data, number_of_threads):
    ThreadsQtdd = number_of_threads
    tamanholista = len(data)
    index = range(0, tamanholista+(tamanholista//ThreadsQtdd), tamanholista//ThreadsQtdd)
    primos = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(ThreadsQtdd):
            futures.append(executor.submit(check_prime, data=data[index[i]:index[i+1]]))
        for future in concurrent.futures.as_completed(futures):
            primos += future.result()
    return primos