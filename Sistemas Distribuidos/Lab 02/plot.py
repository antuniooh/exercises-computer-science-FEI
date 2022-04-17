import matplotlib.pyplot as plt
import numpy as np

class Plot():
    def plot_bar(self, simple_method_quantity, thread_quantity):
        print(thread_quantity)
        legend = ['sem thread', '20 Threads']
        pos = np.arange(len(legend))
        print('pos' + str(pos))
        plt.ylabel('Media de tempo')
        plt.title('metodo X tempo')
        plt.bar(0, simple_method_quantity, color='yellow', edgecolor='black')
        plt.bar(1, thread_quantity, color='blue', edgecolor='black')
        plt.xticks(pos, legend)
        plt.legend(legend, loc=2)
        plt.show()

    def plot_bar_aks(self, simple_method_quantity, thread_quantity):
        print(thread_quantity)
        legend = ['sympy', 'aks']
        pos = np.arange(len(legend))
        print('pos' + str(pos))
        plt.ylabel('Media de tempo')
        plt.title('metodo X tempo')
        plt.bar(0, simple_method_quantity, color='yellow', edgecolor='black')
        plt.bar(1, thread_quantity, color='blue', edgecolor='black')
        plt.xticks(pos, legend)
        plt.legend(legend, loc=2)
        plt.show()

    def plot_threads(self, *args):
        legend = ['5 Threads', '20 Thread', '600 Threads']
        pos = np.arange(len(legend))
        print('pos' + str(pos))
        plt.ylabel(args[4])
        plt.xlabel('Numero de threads')
        plt.title(args[3])
        plt.bar(0, args[0], color='yellow', edgecolor='black')
        plt.bar(1, args[1], color='blue', edgecolor='black')
        plt.bar(2, args[2], color='red', edgecolor='black')
        plt.xticks(pos, legend)
        plt.legend(legend, loc=2)
        plt.show()
