from ImageLib.Image import Image
from ImageLib.ImageHandler import ImageHandler

def main():
    im = Image()
    im.open("./images/P0001460.jpg")
    greyscale = ImageHandler.convert_to_greyscale(im)
    greyscale.save_image("./result/greyscale")
    div = ImageHandler.devide_classes(greyscale)
    print("devision: ", div)
    bin_im = ImageHandler.get_binorized_image(greyscale, div)

    after_erosion = ImageHandler.image_erosion(bin_im, 2)
    after_building = ImageHandler.image_building(after_erosion, 2)

    result_im = ImageHandler.median_filter(after_building)

    result_im.save_image("./result/1")


if __name__ == "__main__":
    main()