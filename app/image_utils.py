# ImageUtils
# @author Paul Ottley
# @copyright 2017

from PIL import Image


class ImageUtils:

    @staticmethod
    def get_dt_captured(f):
        return Image.open(f)._getexif()[36867]

    @staticmethod
    def get_dimensions(f):
        return "{0}{1}{2}".format(Image.open(f)._getexif()[40962], "x",Image.open(f)._getexif()[40963])
