def fut(sig_data):
    def fun(sig_data):
        n = len(sig_data)
        if n == 1:
            return sig_data

        first = []
        second = []

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


def ifut(sig_data):
    def fun(sig_data):
        n = len(sig_data)
        if n == 1:
            return sig_data

        first = []
        second = []

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
