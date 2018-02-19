from transform import FourierTransform
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

N = 8


def _fun(x):
    y = np.cos(x) + np.sin(x)
    return y


def _test():
    n = 600
    # sample spacing
    t = 1.0 / 800.0
    x = np.linspace(0.0, n * t, n)
    y = np.cos(x) + np.sin(x)
    yf = scipy.fftpack.fft(y)
    xf = np.linspace(0.0, 1.0 / (2.0 * t), n / 2)

    fig, ax = plt.subplots()
    ax.plot(xf, 2.0 / n * np.abs(yf[:n // 2]))
    plt.show()


def _main():
    fun_values = FourierTransform._function_values(_fun, 2*np.pi, N)
    dft_values = FourierTransform._dft(FourierTransform, fun_values, 1)
    fft_values = FourierTransform._fft_(FourierTransform, fun_values, 1)

    print(fun_values)


_test()