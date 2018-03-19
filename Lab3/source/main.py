from source.transform import *
import numpy as np
import matplotlib.pyplot as plt

N = 8


def _fun(x):
    y = np.cos(x) + np.sin(x)
    return y


def fast_transform():

    x = np.linspace(0.0, np.pi / 4, 8)
    t = np.linspace(0.0, 2 / np.pi, 8)
    function_values = list(map(lambda i: _fun(i), x))

    transform = fut(function_values)
    reverse_transform = ifut(transform)

    plt.subplot(221)
    plt.plot(x, function_values)
    plt.title('Исходная фенкция')
    plt.grid(True)

    plt.subplot(222)
    plt.plot(t, transform)
    plt.title('БПУ')
    plt.grid(True)

    plt.subplot(223)
    plt.plot(t, reverse_transform)
    plt.title('Обратное БПУ')
    plt.grid(True)

    plt.show()


if __name__ == '__main__':
    print(fut([1,2,3,4,5,6,7,8]))
    #print(fut_left([1,2,3,4,5,6,7,8]))
    print(ifut(fut([1, 2, 3, 4, 5, 6, 7, 8])))

    #fast_transform()
