from ImageLib.Image import Image
import copy


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
    

