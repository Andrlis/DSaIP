import source.Image


class ImageHandler:

    @staticmethod
    def __normalize_pixel_values(r, g, b):
        return min(255, max(0, r)), min(255, max(0, g)), min(255, max(0, b))

    @staticmethod
    def change_brightness(pixels, width, height, br_level):
        for i in range(width):
            for j in range(height):
                r, g, b = map(lambda x: int(x + br_level * x), pixels[i, j])
                r, g, b = ImageHandler.__normalize_pixel_values(r, g, b)
                pixels[i, j] = (r, g, b)
        return pixels

    @staticmethod
    def image_binarization(pixels, width, height,):
        d = width / 8
        t = 0.15
        integral_image = [[0] * width for i in range(height)]

        for i in range(width):
            s = 0
            for j in range(height):
                s += pixels[i, j][0]
                if i == 0:
                    integral_image[j][i] = s
                else:
                    integral_image[j][i] = integral_image[j][i - 1] + s

        for i in range(width):
            for j in range(height):
                x1, y1 = int(i - d), int(j - d)
                x2, y2 = int(i + d), int(j + d)

                x1 = max(0, x1)
                y1 = max(0, y1)
                x2 = min(width - 1, x2)
                y2 = min(height - 1, y2)

                count = (x2 - x1) * (y2 - y1)
                s = integral_image[y2][x2] - integral_image[y1][x2] - integral_image[y2][x1] + integral_image[y1][x1]

                if pixels[i, j][0] * count < s * (1 - t):
                    pixels[i, j] = 0, 0, 0
                else:
                    pixels[i, j] = 255, 255, 255

        return pixels

    # @staticmethod
    # def image_erosion(im_pixels, level=1):
    #     def erosion(pixels)

    # @staticmethod
    # def get_image_border(pixels, width, height):


