# from PIL import Image
#
#
# class Image:
#
#     def __init__(self, name=None, image=None):
#         if image is None:
#             self.image = Image.open(name)
#         else:
#             self.image = image.copy()
#
#         self.width, self.hight = self.image.size
#         self.pixels = self.image.load()
#
#     def get_width(self):
#         return self.width
#
#     def get_hight(self):
#         return self.hight
#
#     def get_size(self):
#         return self.image.size
#
#     def get_pixel_channels(self, x, y):
#         return [self.pixels[x, y][0], self.pixels[x, y][1], self.pixels[x, y][2]]
#
#     def save(self, path, name, format='.jpg'):
#         self.image.save(path + "\\" + name + format)
#
#     def copy(self):
#         return Image(image=self.image)
#
#     def get_pixels(self):
#         return self.pixels
