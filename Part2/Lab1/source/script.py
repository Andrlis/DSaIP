from PIL import Image
from pylab import *
from source.ImageTransform import ImageTransform
import matplotlib.pyplot as plt
import math


def build_histogram(image, channel=0):
    pixels = image.load()
    brightness = [0] * 256

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            brightness[pixels[i, j][channel]] += 1

    plt.hist(range(256), weights=brightness, color='blue')
    plt.show()


def main():
    image = Image.open("../resources/Minsk2.jpg")
    image.show()
    im1 = ImageTransform.convert_to_grayscale(image)
    # convert_to_negative(image)
    # build_histogram(image)
    # im1 = gscale_logarithmic_correction(im1, 50)
    #image = ImageTransform.logarithmic_correction(image, 20)
    im1 = ImageTransform.image_binarization(im1)
    #image.show()
    im1.show()
    # image.show()


if __name__ == "__main__":
    main()
