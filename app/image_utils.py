# ImageUtils
# @author Paul Ottley
# @copyright 2017
import os
from sys import stderr

from PIL import Image
from PIL.ExifTags import TAGS
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata


class ImageUtils:

    @staticmethod
    def get_exif_field(exif, field):
        for (k, v) in exif:
            print('%s = %s' % (TAGS.get(k), v))
            if TAGS.get(k) == field:
                return v

        return "00:00:00"

    @staticmethod
    def get_dt_captured(f):
        dt = ""

        # for (k, v) in Image.open(f)._getexif().items():
        #    print('%s = %s' % (TAGS.get(k), v))

        if os.path.isfile(f):
            print(f)
            try:
                exif = Image.open(f)._getexif().items()
                dt = ImageUtils.get_exif_field(exif, 'DateTimeOriginal')

                # dt = Image.open(f)._getexif()[36867]
            except FileNotFoundError:
                print("Error capturing date taken")
                dt = "-01:00:00"
            except OSError:
                print("Error identifying file as an image")
                dt = "-02:00:00"
            except AttributeError:
                print("File does not contain exif data")
                dt = "-03:00:00"
            except KeyError:
                print("Exif Key was not valid for this file")
                dt = "-04:00:00"
        print("Date: " + str(dt))
        return dt

    @staticmethod
    def get_vid_metadata(f):
        parser = createParser(f)
        if not parser:
            print("Unable to parse file", file=stderr)
            exit(1)

        with parser:
            try:
                metadata = extractMetadata(parser)
            except Exception as err:
                print("Metadata extraction error: %s" % err)
                metadata = None
        if not metadata:
            print("Unable to extract metadata")
            exit(1)

        for line in metadata.exportPlaintext():
            print(line)


    @staticmethod
    def get_dt_captured_split(f):
        dt = ImageUtils.get_dt_captured(f)
        dt_split = None
        if dt is not None:
            dt_split = dt.split(":")
        return dt_split

    @staticmethod
    def get_dimensions(f):
        return "{0}{1}{2}".format(Image.open(f)._getexif()[40962], "x",Image.open(f)._getexif()[40963])
