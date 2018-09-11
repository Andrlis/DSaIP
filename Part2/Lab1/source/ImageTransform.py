import math


class ImageTransform:

    @staticmethod
    def logarithmic_correction(image, constant, image_type='RGB'):

        def gscale_logarithmic_correction(image, constant):
            im = image.copy()
            pixels = im.load()

            for i in range(im.size[0]):
                for j in range(im.size[1]):
                    f = pixels[i, j][0]
                    g = constant * math.log(1 + f)
                    pixels[i, j] = (int(g), int(g), int(g))
            return im

        def rgb_logarithmic_correction(image, constant):
            im = image.copy()
            pixels = im.load()

            for i in range(im.size[0]):
                for j in range(im.size[1]):
                    rgb = [pixels[i, j][0], pixels[i, j][1], pixels[i, j][2]]
                    for channel in range(len(rgb)):
                        rgb[channel] = constant * math.log(1 + rgb[channel])
                    pixels[i, j] = (int(rgb[0]), int(rgb[1]), int(rgb[2]))
            return im

        if image_type == 'RGB':
            return rgb_logarithmic_correction(image, constant)
        elif image_type == 'GRAYSCALE':
            return gscale_logarithmic_correction(image, constant)

    @staticmethod
    def convert_to_grayscale(image):
        im = image.copy()
        pix = im.load()

        for i in range(im.size[0]):
            for j in range(im.size[1]):
                r = pix[i, j][0]
                g = pix[i, j][1]
                b = pix[i, j][2]

                gray = (r * 0.3 + g * 0.59 + b * 0.11)
                pix[i, j] = (int(gray), int(gray), int(gray))

        return im

    @staticmethod
    def convert_to_negative(image):
        im = image.copy()
        pixels = im.load()

        for i in range(im.size[0]):
            for j in range(im.size[1]):
                r = pixels[i, j][0]
                g = pixels[i, j][1]
                b = pixels[i, j][2]

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

                if x1 < 0:
                    x1 = 0
                if x2 >= w:
                    x2 = w - 1
                if y1 < 0:
                    y1 = 0
                if y2 >= h:
                    y2 = h - 1

                count = (x2 - x1) * (y2 - y1)
                s = integral_image[y2][x2] - integral_image[y1][x2] - integral_image[y2][x1] + integral_image[y1][x1]

                if pixels[i, j][0] * count < s * (1 - t):
                    pixels[i, j] = 0, 0, 0
                else:
                    pixels[i, j] = 255, 255, 255

        return im

    @staticmethod
    def brightness_section(image, gmin=0, gmax=0):
        im = image.copy()
        w, h = im.size

        #for i in range(w):
