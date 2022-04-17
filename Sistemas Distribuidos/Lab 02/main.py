from prime import *
from time import perf_counter_ns
from plot import Plot
import numpy as np

plot = Plot()

def get_time(data):
    start = perf_counter_ns()
    primes = is_prime(data)
    finish = perf_counter_ns()
    return (finish - start)/1000000, primes, finish - start

def get_time_t(data, number_of_threads=5):
    start = perf_counter_ns()
    primes = is_prime_thread(data, number_of_threads)
    finish = perf_counter_ns()
    return (finish - start)/1000000, primes, finish - start

def main():
    simple_array = []
    thread_array = []
    thread_20_array = []
    thread_600_array = []

    simple_array_speedup = []
    thread_array_speedup = []
    thread_20_array_speedup = []
    thread_600_array_speedup = []

    with open("dataset/data.csv") as file:
        data = [line.strip() for line in file]
    data = list(map(int, data))

    print('\n\nanalise de %d valores\n\n'%(len(data)))

    number_t = int(input("Digite o número de threads desejada"))

    for i in range(50):

        # serial
        tempo_ms_serial, primo_sp, tempo_exec_serial = get_time(data)
        simple_array.append(tempo_ms_serial)

        # paralel
        tempo_ms_threads5, primo_mt, tempo_exec_threads5 = get_time_t(data, number_t)
        tempo_ms_threads20, primo_mt, tempo_exer_threads20 = get_time_t(data, 20)
        tempo_ms_threads600, primo_mt, tempo_exer_threads600 = get_time_t(data, 600)

        thread_array.append(tempo_ms_threads5)
        thread_20_array.append(tempo_ms_threads20)
        thread_600_array.append(tempo_ms_threads600)

        simple_array_speedup.append(tempo_exec_serial/tempo_exec_serial)
        thread_array_speedup.append(tempo_exec_serial/tempo_exec_threads5)
        thread_20_array_speedup.append(tempo_exec_serial/tempo_exer_threads20)
        thread_600_array_speedup.append(tempo_exec_serial/tempo_exer_threads600)

    media_tempo_s = np.mean(simple_array_speedup)

    plot.plot_bar(np.mean(simple_array), np.mean(thread_20_array))
    plot.plot_threads(np.mean(thread_array), np.mean(thread_20_array), np.mean(thread_600_array), "Tempo X threads", "Media de tempo")
    plot.plot_threads(np.mean(thread_array_speedup), np.mean(thread_20_array_speedup), np.mean(thread_600_array_speedup), "ApeedUp X threads", "SpeedUp")

    threads = 20
    speed_up = np.mean(thread_20_array_speedup)
    '''
    Fs = n - s
         -----
         n *  (s - 1)
    '''
    serial_fraction = (threads - speed_up) / ((threads-1) * speed_up)
    print(serial_fraction)


if __name__ == '__main__':
    main()