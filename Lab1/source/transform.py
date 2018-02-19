import cmath
import math


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
    def _dft(self, _values, direction_):
        self.count = 0
        if abs(direction_) != 1:
            return [0]

        n = len(_values)
        out_values = [0] * n
        for k in range(n):
            for j in range(n):
                out_values[k] += (_values[j] * cmath.exp( (-1) * direction_ * 2 * cmath.pi * complex(0, 1) * k / n))
                self.count += 1
            if direction_ == -1:
                out_values[k] /= n

        return list(out_values)

    @staticmethod
    def _fft_(self, _in_values, direction):
        self.count = 0
        out_values = self._fft(self, _in_values, direction)
        reordered_values = self._fft_reorder(self, out_values, len(out_values))
        return reordered_values

    @staticmethod
    def _fft(self, _values, direction_):
        n = len(_values)
        if n == 1:
            return _values

        _val1 = [complex(0, 0)] * (int(n / 2) + n % 2)
        _val2 = [complex(0, 0)] * (int(n / 2))

        for i in range(n):
            if i % 2 == 0:
                _val1[int(i / 2)] = _values[i]
            else:
                _val2[int(i / 2)] = _values[i]

        _b1 = self._fft(self, _val1, direction_)
        _b2 = self._fft(self, _val2, direction_)

        w_n = complex(cmath.cos(2 * cmath.pi / n), direction_ * cmath.sin(2 * cmath.pi / n))
        w = complex(1, 0)
        y = [complex(0, 0)] * n

        for i in range(int(n / 2)):
            y[i] = _b1[i] + _b2[i] * w
            y[i + int(n / 2)] = _b1[i] - _b2[i] * w
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
        r = 0;
        while step != 0:
            r = r << 1
            r = r + (x & 1)
            x = x >> 1
            step = step - 1

        return r
