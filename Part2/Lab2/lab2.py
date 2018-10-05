from PIL import Image
from source.ImageHandler import ImageHandler
from source.ImageFilter import ImageFilter

images = ["P0001460"]


def process_image(index):
    s_image = Image.open("./images/" + images[index] + ".jpg")
    width, height = s_image.size

    image = s_image.copy()
    #s_image.show()
    ImageHandler.change_brightness(image.load(), width, height, 0.5)
    ImageFilter.high_frequency_filter(image.load(), width, height)
    #ImageFilter.median_filter(image.load(), width, height)
    #ImageFilter.low_frequency_filter(image.load(), width, height)
    ImageHandler.convert_to_grayscale(image.load(), width, height)
    level = ImageHandler.get_mean_brightness(image.load(), width, height)
    #ImageHandler.binarization(image.load(), width, height, level)

    #ImageFilter.median_filter(image.load(), width, height)
    #ImageFilter.high_frequency_filter(image.load(), width, height)
    #ImageHandler.image_binarization(image.load(), width, height)


    # s_image.show()
    image.show()


def main():
    for index in range(len(images)):
        process_image(index)


if __name__ == "__main__":
    main()
