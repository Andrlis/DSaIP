import math
import random


class ImageTransform:

    @staticmethod
    def __normalize_pixel_values(r, g, b):
        return min(255, max(0, r)), min(255, max(0, g)), min(255, max(0, b))

    @staticmethod
    def logarithmic_correction(image):
        constant = input('Enter constant:')
        im = image.copy()
        pixels = im.load()

        for i in range(im.size[0]):
            for j in range(im.size[1]):
                pixels[i, j] = tuple(map(lambda x: int(constant * math.log(1 + x)), pixels[i, j]))
        return im

    @staticmethod
    def convert_to_grayscale(image):
        im = image.copy()
        pix = im.load()

        for i in range(im.size[0]):
            for j in range(im.size[1]):
                r, g, b = pix[i, j]

                gray = (r * 0.3 + g * 0.59 + b * 0.11)
                pix[i, j] = (int(gray), int(gray), int(gray))

        return im

    @staticmethod
    def convert_to_negative(image):
        im = image.copy()
        pixels = im.load()

        for i in range(im.size[0]):
            for j in range(im.size[1]):
                r, g, b = pixels[i, j]

                pixels[i, j] = (255 - r, 255 - g, 255 - b)

        return im

    @staticmethod
    def image_binarization(image):
        im = image.copy()
        w, h = im.size
        pixels = im.load()

        d = w / 8
        t = 0.15
        integral_image = [[0] * w for i in range(h)]

        for i in range(w):
            s = 0
            for j in range(h):
                s += pixels[i, j][0]
                if i == 0:
                    integral_image[j][i] = s
                else:
                    integral_image[j][i] = integral_image[j][i - 1] + s

        for i in range(w):
            for j in range(h):
                x1, y1 = int(i - d), int(j - d)
                x2, y2 = int(i + d), int(j + d)

                x1 = max(0, x1)
                y1 = max(0, y1)
                x2 = min(w - 1, x2)
                y2 = min(h - 1, y2)

                count = (x2 - x1) * (y2 - y1)
                s = integral_image[y2][x2] - integral_image[y1][x2] - integral_image[y2][x1] + integral_image[y1][x1]

                if pixels[i, j][0] * count < s * (1 - t):
                    pixels[i, j] = 0, 0, 0
                else:
                    pixels[i, j] = 255, 255, 255

        return im

    @staticmethod
    def change_brightness(image):
        br_level = input('Brightness level:')
        im = image.copy()
        pixels = im.load()
        w, h = im.size

        for i in range(w):
            for j in range(h):
                r, g, b = map(lambda x: int(x + br_level * x), pixels[i, j])
                r, g, b = ImageTransform.__normalize_pixel_values(r, g, b)
                pixels[i, j] = (r, g, b)
        return im

    @staticmethod
    def change_contrast(image):
        contrast = input('Contrast level:')
        im = image.copy()
        pixels = im.load()
        w, h = im.size

        avg_brightness = 0
        for i in range(w):
            for j in range(h):
                r, g, b = pixels[i, j]
                avg_brightness += r * 0.299 + g * 0.587 + b * 0.114
        avg_brightness /= w * h

        palette = []
        for i in range(256):
            temp = int(avg_brightness + contrast * (i - avg_brightness))
            temp = min(255, max(0, temp))
            palette.append(temp)

        for i in range(w):
            for j in range(h):
                r, g, b = pixels[i, j]
                pixels[i, j] = (palette[r], palette[g], palette[b])

        return im

    @staticmethod
    def add_noise(image):
        im = image.copy()
        w, h = im.size
        pixels = im.load()

        for i in range(w):
            for j in range(h):
                rand = random.randint(-255, 255)
                r, g, b = map(lambda x: x + rand, pixels[i, j])
                r, g, b = ImageTransform.__normalize_pixel_values(r, g, b)

            pixels[i, j] = (r, g, b)

        return im
