import numpy as nm

radem = [[1, 1, 1, 1, -1, -1, -1, -1], [1, 1, -1, -1, 1, 1, -1, -1], [1, -1, 1, -1, 1, -1, 1, -1]]


def create_current_matrix(matrix):
    l = len(matrix)
    result = nm.empty([l * 2, l * 2], dtype=int)

    for r in range(l):
        for c in range(l):
            result[r][c] = result[r + l][c] = result[r][c + l] = matrix[r][c]
            result[r + l][c + l] = - matrix[r][c]

    return result


def get_matrix(coef):
    if coef == 0:
        return [[1]]
    else:
        prev_matr = get_matrix(coef - 1)
        return create_current_matrix(prev_matr)


def fut_left(sig_data):
    def fun(sig_data):
        n = len(sig_data)
        if n == 1:
            return sig_data

        first = [] * int(n / 2)
        second = [] * int(n / 2)

        for i in range(int(n / 2)):
            first.append(sig_data[i] + sig_data[i + int(n / 2)])
            second.append(sig_data[i] - sig_data[i + int(n / 2)])

        first_t = fun(first)
        second_t = fun(second)

        result = [0] * n
        for i in range(int(n / 2)):
            result[i] = first_t[i]
            result[i + int(n / 2)] = second_t[i]

        return result

    return fun(sig_data)


def ifut_left(sig_data):
    def fun(sig_data):
        n = len(sig_data)
        if n == 1:
            return sig_data

        first = [] * int(n / 2)
        second = [] * int(n / 2)

        for i in range(int(n / 2)):
            first.append(sig_data[i])
            second.append(sig_data[i + int(n / 2)])

        first_t = fun(first)
        second_t = fun(second)

        result = [0] * n
        for i in range(int(n / 2)):
            result[i] = (first_t[i] + second_t[i]) / 2
            result[i + int(n / 2)] = (first_t[i] - second_t[i]) / 2

        return result

    return fun(sig_data)


def ifut(signal):
    def fun(a):
        l = len(a)
        if l == 1:
            return a
        else:
            up = fun(a[0:int(l / 2)])
            down = fun(a[int(l / 2):l])
            return list(map(lambda x, y: x + y, up, down)) + list(map(lambda x, y: x - y, up, down))

    return fun(signal)


def fut(signal):
    def fun(a):
        l = len(a)
        if l == 1:
            return a
        else:
            up = fun(a[0:int(l / 2)])
            down = fun(a[int(l / 2):l])
            return list(map(lambda x, y: x + y, up, down)) + list(map(lambda x, y: x - y, up, down))

    return list(map(lambda x: x / 8, fun(signal)))
