from source.transform import *
import numpy as np
import matplotlib.pyplot as plt

N = 8


def _fun(x):
    y = np.cos(x) + np.sin(x)
    return y


def fast_transform():
    wal = get_wal_fans()
    print('Функции Уолша, упорядоченные по частоте')
    for w in wal:

        s = ''
        for i in range(len(w)):
            if w[i] == 1:
                s += '+'
            else:
                s += '-'
        print(s)

    print('Функции Уолша, упорядоченные по Адамару')
    ad_matr = get_matrix(3)
    for m in ad_matr:
        s = ''
        for c in m:
            if c == 1:
                s += '+'
            else:
                s += '-'
        print(s)

    x = np.linspace(0.0, 2 * np.pi, 8)
    function_values = list(map(lambda i: _fun(i), x))

    transform = fut(function_values)
    reverse_transform = ifut(transform)

    plt.tight_layout()

    plt.subplot(221)
    plt.plot(x, function_values)
    plt.title('Исходная функция')
    plt.grid(True)

    plt.subplot(222)
    plt.plot(x, transform)
    plt.title('БПУ')
    plt.grid(True)

    plt.subplot(223)
    plt.plot(x, reverse_transform)
    plt.title('Обратное БПУ')
    plt.grid(True)

    plt.show()


def discrete_transform():
    x = np.linspace(0.0, 2 * np.pi, 8)
    function_values = list(map(lambda i: _fun(i), x))

    transform = dut(function_values)
    reverse_transform = idut(transform)

    plt.tight_layout()

    plt.subplot(221)
    plt.plot(x, function_values)
    plt.title('Исходная функция')
    plt.grid(True)

    plt.subplot(222)
    plt.plot(x, transform)
    plt.title('ДПУ')
    plt.grid(True)

    plt.subplot(223)
    plt.plot(x, reverse_transform)
    plt.title('Обратное ДПУ')
    plt.grid(True)

    plt.show()


if __name__ == '__main__':
    fast_transform()
    discrete_transform()
