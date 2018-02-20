from transform import FourierTransform
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import cmath

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


def discrete_transform(_values):
    f, axarr = plt.subplots(2, 2, figsize=(8, 6))
    plt.tight_layout()

    x = np.linspace(0.0, np.pi/4, 8)
    dft_values = FourierTransform._dft(FourierTransform, _values, 1)
    idft_values = FourierTransform._dft(FourierTransform, dft_values, -1)

    pol = list(map(lambda x: cmath.polar(x), dft_values))

    ph_val = []
    amp_val = []

    for i in range(len(dft_values)):
        amp_val.append(pol[i][0])
        ph_val.append(pol[i][1])

    axarr[0, 0].plot(x, _values)
    axarr[0, 0].set_title('Исходная функция')
    axarr[0, 0].grid(True)

    axarr[0, 1].plot(x, amp_val)
    axarr[0, 1].set_title('Амплитудный спект')
    axarr[0, 1].grid(True)

    axarr[1, 0].plot(x, ph_val)
    axarr[1, 0].set_title('Фазовый спектр')
    axarr[1, 0].grid(True)

    axarr[1, 1].plot(x, idft_values)
    axarr[1, 1].set_title('Обратное преобразование')
    axarr[1, 1].grid(True)

    plt.show()


def fast_transform(_values):
    f, axarr = plt.subplots(2, 2, figsize=(8, 6))
    plt.tight_layout()

    x = np.linspace(0.0, np.pi / 4, 8)
    fft_values = FourierTransform._fft(FourierTransform, _values, 1)
    ifft_values = FourierTransform._fft(FourierTransform, fft_values, -1)

    pol = list(map(lambda x: cmath.polar(x), fft_values))

    ph_val = []
    amp_val = []

    for i in range(len(fft_values)):
        amp_val.append(pol[i][0])
        ph_val.append(pol[i][1])

    axarr[0, 0].plot(x, _values)
    axarr[0, 0].set_title('Исходная функция')
    axarr[0, 0].grid(True)

    axarr[0, 1].plot(x, amp_val)
    axarr[0, 1].set_title('Амплитудный спект')
    axarr[0, 1].grid(True)

    axarr[1, 0].plot(x, ph_val)
    axarr[1, 0].set_title('Фазовый спектр')
    axarr[1, 0].grid(True)

    axarr[1, 1].plot(x, ifft_values)
    axarr[1, 1].set_title('Обратное преобразование')
    axarr[1, 1].grid(True)

    plt.show()


def _main():
    fun_values = FourierTransform._function_values(_fun, 2 * np.pi, N)
    discrete_transform(fun_values)
    print('DFF number of operations:', FourierTransform.count)
    fast_transform(fun_values)
    print('FFT number of operations:', FourierTransform.count)


_main()
