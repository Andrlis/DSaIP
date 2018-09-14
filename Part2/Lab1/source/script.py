from PIL import Image
from source.ImageTransform import ImageTransform
from source.ImageFilter import ImageFilter
import matplotlib.pyplot as plt


def build_histogram(image, channel=0):
    pixels = image.load()
    brightness = [0] * 256

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            brightness[pixels[i, j][channel]] += 1

    plt.hist(range(256), weights=brightness, color='blue')
    plt.show()


def main():
    image = Image.open("../resources/im3.jpg")
    #image.show()
    #im1 = ImageTransform.convert_to_grayscale(image)
    # convert_to_negative(image)
    # build_histogram(image)
    #image = ImageTransform.logarithmic_correction(image, 20)
    #im1 = ImageTransform.image_binarization(im1)
    #im1 = ImageFilter.roberts_operator(im1)
    #im1 = ImageTransform.convert_to_negative(im1)
    #im1 = ImageTransform.change_contrast(im1, 8)
    #im1 = ImageTransform.change_brightness(im1, -0.3)
    im1 = ImageFilter.high_frequency_filter(image)
    #image.show()
    im1.show()
    # image.show()


if __name__ == "__main__":
    main()
