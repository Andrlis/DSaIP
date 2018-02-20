import cmath
import math
import numpy


class FourierTransform:
    count = 0

    @staticmethod
    def _function_values(function_, period_, n_):
        interval = period_ / n_
        func_values = []

        x = complex(0, 0)
        for i in range(n_):
            func_values.append(function_(x))
            x += interval

        return func_values

    @staticmethod
    def _dft(self, _values, direction):
        self.count = 0

        n = len(_values)
        _out_values = [complex(0, 0)] * n

        for k in range(n):
            for j in range(n):
                _out_values[k] += _values[j] * cmath.e **(direction * complex(0, -1) * 2 * cmath.pi * k * j / n)
                self.count += 1
            if direction == -1:
                _out_values[k] /= n

        return _out_values


    @staticmethod
    def _fft(self, _in_values, direction):
        self.count = 0
        _out_values = self._fft_(self, _in_values, direction)

        if direction == -1:
            n = len(_in_values)
            for i in range(n):
                _out_values[i] /= n

        return _out_values


    @staticmethod
    def _fft_(self, _values, direction):
        n = len(_values)

        if n == 1:
            return _values

        _values_even = [complex(0, 0)] * (int(n / 2))
        _values_odd = [complex(0, 0)] * (int(n / 2))

        for i in range(n):
            if i % 2 == 0:
                _values_even[int(i / 2)] = _values[i]
            else:
                _values_odd[int(i / 2)] = _values[i]

        _b_even = self._fft_(self, _values_even, direction)
        _b_odd = self._fft_(self, _values_odd, direction)

        w_n = complex(cmath.exp(direction * (-1) * 2 * cmath.pi * complex(0, 1) / n))
        w = 1
        y = [complex(0, 0)] * n

        for i in range(int(n / 2)):
            y[i] = _b_even[i] + _b_odd[i] * w
            y[i + int(n / 2)] = _b_even[i] - _b_odd[i] * w
            w = w * w_n
            self.count += 1

        return y


    @staticmethod
    def _fft_reorder(self, _data, _len):
        if _len <= 2:
            return
        r = 0
        for x in range(_len):
            r = self.rev_next(x, _len)
            if r > x:
                temp = _data[x]
                _data[x] = _data[r]
                _data[r] = temp

        return _data


    @staticmethod
    def rev_next(x, n):
        step = math.log2(n)
        r = 0
        while step != 0:
            r = r << 1
            r = r + (x & 1)
            x = x >> 1
            step = step - 1

        return r
