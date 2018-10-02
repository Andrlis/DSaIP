from PIL import Image
from pylab import *
from source.ImageTransform import ImageTransform
from source.ImageFilter import ImageFilter
import matplotlib.pyplot as plt


def build_histogram(image, channel=0):
    pixels = image.load()
    brightness = [0] * 256

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            brightness[pixels[i, j][channel]] += 1

    colors = {
        0: 'red',
        1: 'green',
        2: 'blue'
    }

    plt.plot(range(256), brightness, color=colors[channel])
    plt.show()


menu_items = {
    1: ImageTransform.convert_to_grayscale,
    2: ImageTransform.image_binarization,
    3: ImageTransform.convert_to_negative,
    4: ImageTransform.logarithmic_correction,
    5: ImageTransform.change_brightness,
    6: ImageTransform.change_contrast,
    7: ImageFilter.low_frequency_filter,
    8: ImageFilter.high_frequency_filter,
    9: ImageFilter.roberts_operator,
}


def image_processing(image, im_function):
    image.show()
    im = im_function(image=image)
    im.show()
    if input('Save image? (y/n)') == 'y':
        im.save("../resources/" + input("Enter name:") + ".jpg")


def menu(image):
    m = input("""
            1 - Convert to grayscale
            2 - Binarization
            3 - Convert to negative
            4 - Logarithmic correction
            5 - Change brightness
            6 - Change contrast
            7 - Low frequency filter
            8 - Height frequency filter
            9 - Robert`s operator""")

    image_processing(image, menu_items[int(m)])


def main():
    image = Image.open("../resources/im3.jpg")

    build_histogram(image, 0)
    build_histogram(image, 1)
    build_histogram(image, 2)

    while True:
        menu(image)


if __name__ == "__main__":
    main()
