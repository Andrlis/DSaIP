import numpy as np
from transform import FourierTransform


def _fun(x):
    y = np.cos(x) + np.sin(x)
    return y


def _add_noise(data, noise):
    return lambda x: x + noise, data


def blackman_filter(signal):
    fc = 0.1  # Cutoff frequency as a fraction of the sampling rate (in (0, 0.5)).
    b = 0.08  # Transition band, as a fraction of the sampling rate (in (0, 0.5)).
    N = int(np.ceil((4 / b)))
    if not N % 2: N += 1  # Make sure that N is odd.
    n = np.arange(N)

    # Compute sinc filter.
    h = np.sinc(2 * fc * (n - (N - 1) / 2.))

    # Окно Блэкмана
    w = 0.42 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) + 0.08 * np.cos(4 * np.pi * n / (N - 1))

    # Multiply sinc filter with window.
    h = h * w

    # Нормализация
    h = h / np.sum(h)

    return np.convolve(signal, h)


