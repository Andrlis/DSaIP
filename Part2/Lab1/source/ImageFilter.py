import math


class ImageFilter:

    @staticmethod
    def roberts_operator(image):
        im = image.copy()
        pixels = im.load()
        w, h = im.size

        for i in range(w - 1):
            for j in range(h - 1):
                pixels[i, j] = tuple(
                    map(lambda x1, x2, x3, x4: int(math.sqrt((x1 - x2) ** 2 + (x2 - x3) ** 2)), pixels[i + 1, j],
                        pixels[i, j + 1], pixels[i, j], pixels[i + 1, j + 1]))

        return im

    @staticmethod
    def __filter(pixels, i, j, kernel, div):
        kernel_size = len(kernel)
        shift = (kernel_size - 1) / 2
        s = (0, 0, 0)

        for x in range(kernel_size):
            for y in range(kernel_size):
                g = tuple(map(lambda f, h: f * h, pixels[i - shift + x, j - shift + y], kernel[x][y]))
                s = tuple(map(lambda x1, x2: x1 + x2, g, s))

        return tuple(map(lambda x: int(x * div), s))

    @staticmethod
    def low_frequency_filter(image):
        kernel = [[(1, 1, 1)] * 3 for i in range(3)]
        div = 1 / 9
        im = image.copy()
        pxl = im.load()
        w, h = im.size

        for i in range(1, w - 1):
            for j in range(1, h - 1):
                pxl[i, j] = ImageFilter.__filter(pxl, i, j, kernel, div)
        return im

    @staticmethod
    def high_frequency_filter(image):
        kernel = [[(-1,) * 3, (-1,) * 3, (-1,) * 3], [(-1,) * 3, (9,) * 3, (-1,) * 3],
                  [(-1,) * 3, (-1,) * 3, (-1,) * 3]]
        div = 1 / 9
        im = image.copy()
        pxl = im.load()
        w, h = im.size

        for i in range(1, w - 1):
            for j in range(1, h - 1):
                pxl[i, j] = ImageFilter.__filter(pxl, i, j, kernel, div)
        return im
