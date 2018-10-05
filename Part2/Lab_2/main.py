from ImageLib.Image import Image
from ImageLib.ImageHandler import ImageHandler

def main():
    im = Image()
    im.open("./images/P0001460.jpg")
    greyscale = ImageHandler.convert_to_greyscale(im)
    div = ImageHandler.devide_classes(greyscale)
    bin_im = ImageHandler.get_binorized_image(greyscale, div)
    bin_im.save_image("./result/1")


if __name__ == "__main__":
    main()