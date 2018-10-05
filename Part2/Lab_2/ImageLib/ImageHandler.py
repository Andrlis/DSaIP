from ImageLib.Image import Image
import copy
import numpy as np


class ImageHandler:

    @staticmethod
    def convert_to_greyscale(image):
        if image.get_mode() == "RGB":
            result = []
            for i in range(len(image.get_pixels()[0])):
                result.append(int(image.get_pixels()[0][i] * 0.3
                                  + image.get_pixels()[1][i] * 0.59
                                  + image.get_pixels()[2][i] * 0.11))
        else:
            result = copy.copy(image.get_pixels()[0])

        return Image([result], image.get_width(), image.get_height(), "L")

    @staticmethod
    def convert_to_negative(image):
        new_pixels = []
        for channel in image.get_pixels():
            result = []
            for i in range(len(channel)):
                result.append(255 - channel[i])
            new_pixels.append(result)

        return Image(new_pixels, image.get_width(), image.get_height(), image.get_mode())

    @staticmethod
    def __get_neighbors(channel, i, j, width, size=9):
        indent = int(np.sqrt(size)) >> 1

        neighborhood = list()
        for neigh_row in range(j - indent, j + indent + 1):
            for neigh_col in range(i - indent, i + indent + 1):
                neighborhood.append(channel[neigh_row * width + neigh_col])

        return neighborhood

    @staticmethod
    def median_filte(image):
        new_image = []

        for channel in image.get_pixels():
            result = np.zeros(image.get_width() * image.get_height())
            for i in range(1, image.get_width() - 1):
                for j in range(1, image.get_height() - 1):
                    neighbors = ImageHandler.__get_neighbors(channel, i, j, image.get_width())
                    neighbors.sort()
                    result[image.get_width * j + i] = neighbors[int(len(neighbors) / 2)]
            new_image.append(result)

        return new_image

    @staticmethod
    def get_binorized_image(image, division):
        new_channels = list()

        for channel in image.get_channels():
            new_channels.append(list(map(lambda x: 0 if x < division else 255, channel)))

        return Image(new_channels,
                     image.get_height(),
                     image.get_width(),
                     image.get_range_of_brightness())

    @staticmethod
    def __calculate_intensity_sum(histogram):
        sum = 0
        for intensity in range(len(histogram)):
            sum += intensity * histogram[intensity]
        return sum

    @staticmethod
    def devide_classes(image):
        #greyscale_image = ImageHandler.get_greyscale_image(image)
        histogram = image.get_brightness_distribution()

        amount_of_all_pixels = image.get_height() * image.get_width()
        all_intensity_sum = ImageHandler.__calculate_intensity_sum(histogram)

        best_dispersion = 0
        best_division = 0

        first_class_amount_of_pixels = 0
        first_class_itensity = 0

        for current_division in range(len(histogram) - 1):

            first_class_amount_of_pixels += histogram[current_division]
            first_class_itensity += current_division * histogram[current_division]

            first_class_probability = first_class_amount_of_pixels / amount_of_all_pixels
            second_class_probability = 1 - first_class_probability

            first_class_mean = first_class_itensity / first_class_amount_of_pixels
            second_class_mean = (all_intensity_sum - first_class_itensity) / \
                                (amount_of_all_pixels - first_class_amount_of_pixels)

            delta = (first_class_mean - second_class_mean)
            current_dispersion = (delta ** 2) * first_class_probability * second_class_probability

            if current_dispersion > best_dispersion:
                best_dispersion = current_dispersion
                best_division = current_division

        return best_division