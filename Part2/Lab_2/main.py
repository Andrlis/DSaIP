from ImageLib.Image import Image
from ImageLib.ImageHandler import ImageHandler

def main():
    im = Image()
    im.open("./images/P0001460.jpg")
    im = ImageHandler.convert_to_greyscale(im)
    im.save_image("./result/1")


if __name__ == "__main__":
    main()