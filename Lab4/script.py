import numpy as np
import matplotlib.pyplot as plt
from transform import FourierTransform

N = 64


def _fun(x):
    y = np.cos(x) + np.sin(x)
    return y


# def test(signal):
#     fc = 0.1
#     b = 0.06
#     N = int(np.ceil((4 / b)))
#     if not N % 2: N+=1
#     n = np.arange(N)
#
#     h = np.sinc(2*fc*(n-(N-1)/2.))
#
#     w = 0.42 - 0.5*np.cos(2*np.pi*n/(N-1)) + 0.08*np.cos(4*np.pi*n/(N-1))
#
#     h = h * w
#
#     h=h/np.sum(h)
#
#     return list(map(lambda x, y: x*y, signal, h))


def blackman_filter(signal, fd, fs, fx, n):
    # Расчёт импульсной характеристики фильтра
    def get_impulse_response(_fd, _fs, _fx, _n):
        H = [0] * N  # Импульсная характеристика фильтра
        H_id = [0] * N  # Идеальная импульсная характеристика
        W = [0] * N  # Весовая функция

        # Расчет импульсной характеристики
        fc = (fs + fx) / (2 * fd)

        for i in range(N):
            if i == 0:
                H_id[i] = 2 * np.pi * fc
            else:
                H_id[i] = np.sin(2 * np.pi * fc * i) / (np.pi * i)
            # весовая функция Блекмена
            W[i] = 0.42 - 0.5 * np.cos((2 * np.pi * i) / (N - 1)) + 0.08 * np.cos((4 * np.pi * i) / (N - 1))
            H[i] = H_id[i] * W[i]

        return H

    # Result
    imp_resp = get_impulse_response(fd, fs, fx, n)
    filter = imp_resp / np.sum(imp_resp)
    out = [0] * len(signal)

    for i in range(len(signal)):
        for j in range(len(signal) - 1):
            if i >= j:
                out[i] += filter[j] * signal[i - j]

    return out


def _main():
    t = [0] * N
    step = 1 / (4 * np.pi)

    signal = []
    noise = []

    for i in range(N):
        signal.append(_fun(t[i]))
        noise.append(np.sin(10 * t[i]))
        if i < N - 1:
            t[i + 1] = t[i] + step

    # Add noise to signal
    signal_with_noise = list(map(lambda x, y: x + y, signal, noise))

    #############
    n = 20  # Длина фильтра
    #fd = 0.318  # Частота дискретизации входных данных
    fd = 1000
    fs = 1 / (4 * np.pi)  # Частота полосы пропускания
    fx = 50  # Частота полосы затухания

    result = blackman_filter(signal_with_noise, fd, fs, fx, n)
    #############

    f, axarr = plt.subplots(2, 2, figsize=(8, 6))
    plt.tight_layout()

    axarr[0, 0].plot(t, signal)
    axarr[0, 0].set_title('Signal without noise')
    axarr[0, 0].grid(True)

    axarr[0, 1].plot(t, signal_with_noise)
    axarr[0, 1].set_title('Signal with noise')
    axarr[0, 1].grid(True)

    axarr[1, 0].plot(t, result)
    axarr[1, 0].set_title('Blackman`s filter')
    axarr[1, 0].grid(True)

    # axarr[1, 1].plot(t, after_bm_filter)
    # axarr[1, 1].set_title('Blackman`s filter test')
    # axarr[1, 1].grid(True)

    plt.show()


if __name__ == "__main__":
    _main()
