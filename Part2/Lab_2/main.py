import sys

from ImageLib.Image import Image
from ImageLib.ImageHandler import ImageHandler
from ImageLib.ObjectHandler import ObjectHandler


def main():
    sys.setrecursionlimit(1048576)

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

    objects = ObjectHandler.find_object(after_building)

    vectors = []
    for i in range(len(objects)):
        vectors.append((i, objects[i].get_vector()))

    #normalization
    normalize_vectors = []
    for v in vectors:
        normalize_vectors.append((v[0], []))
    for i in range(len(vectors[0][1])):
        array = []
        for v in vectors:
            array.append(v[1][i])

        min_value = min(array)
        max_value = max(array)

        for j in range(len(vectors)):
            normalize_vectors[j][1].append((vectors[j][1][i] - min_value) / (max_value - min_value))

    # result_im.save_image("./result/1")


if __name__ == "__main__":
    main()
