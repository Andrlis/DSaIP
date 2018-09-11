import PIL


class Image:

    def __init__(self, name):
        self.image_name = name
        self.image = PIL.Image.open(self.image_name)
        self.width, self.hight = self.image.size

    def open(self, name):
        self.image = PIL.Image.open(name)
        self.width, self.hight = self.image.size

    def get_width(self):
        return self.width

    def get_hight(self):
        return self.get_hight()

    def get_pixel_channels(self, x, y):
        pixels = self.image.load()
        return [pixels[x, y][0], pixels[x, y][1], pixels[x, y][2]]

    def save(self, path, name, format='.jpg'):
        self.image.save(path + "\\" + name + format)

    def copy(self, image):
        self.image = image.copy()
        self.width = image.size[1]
        self.hight = image.size[0]

    def get_pixels(self):
        return self.image.load()