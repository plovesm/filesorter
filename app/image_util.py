# ImageUtils
# @author Paul Ottley
# @copyright 2017
import os

from PIL import Image
from PIL.ExifTags import TAGS
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata


class ImageUtils:

    @staticmethod
    def get_exif_field(exif, field):
        for (k, v) in exif:
            # print('%s = %s' % (TAGS.get(k), v))
            if TAGS.get(k) == field:
                return v

        return "0A:00:00"

    @staticmethod
    def get_dt_captured(f):
        dt = ""

        # for (k, v) in Image.open(f)._getexif().items():
        #    print('%s = %s' % (TAGS.get(k), v))

        if os.path.isfile(f):
            try:
                exif = Image.open(f)._getexif().items()
                dt = ImageUtils.get_exif_field(exif, 'DateTimeOriginal')
                if dt == "0A:00:00" or dt is None:
                    # print("No date found. Trying different method.")
                    dt = ImageUtils.get_alt_metadata2(f)
                # dt = Image.open(f)._getexif()[36867]
            except Exception as err:
                # print("get_dt_captured(): Metadata extraction error: %s" % err)
                dt = ImageUtils.get_alt_metadata(f)

        return dt

    @staticmethod
    def get_alt_metadata(f):
        dt = "0B:00:00"
        try:
            parser = createParser(f)
            if not parser:
                # print("Unable to parse file")
                dt = "0P:00:00"

            with parser:
                try:
                    metadata = extractMetadata(parser)
                    #TODO Do something with metadata
                    for line in metadata.exportPlaintext():
                        if "Creation date" in line:
                            dt = line.split("- Creation date: ")[1]
                            dt2 = dt.split(" ")[0].replace("-", ":")
                            print("File: " + f + " Date fixed: " + dt2)
                            dt = dt2
                except Exception as err:
                    print("Metadata extraction error: %s" % err)
                    metadata = None
            if not metadata:
                # print("Unable to extract metadata")
                dt = "0M:00:00"
            """
            for line in metadata.exportPlaintext():
                if "Creation date" in line:
                    dt = line.split("- Creation date: ")[1]
                print(line)
            """
        except Exception as err2:
            print("Error creating Parser: %s" % err2)
        return dt

    @staticmethod
    def get_alt_metadata2(filename):

        filename, realname = filename, filename
        parser = createParser(filename, realname)
        if not parser:
            print
            "Unable to parse file"
            exit(1)
        try:
            metadata = extractMetadata(parser)
        except Exception as err:
            print("Metadata extraction error: %s" % err)
            metadata = None
        if not metadata:
            print
            "Unable to extract metadata"
            exit(1)

        text = metadata.exportPlaintext()

        for line in text:
            print(line)

        return metadata

    @staticmethod
    def get_dt_captured_split(f):
        dt = ImageUtils.get_dt_captured(f)
        dt_split = []
        if dt is not None:
            if "-" in dt:
                dt_split = dt.split("-")
            else:
                dt_split = dt.split(":")
        if dt_split is None or len(dt_split) < 2:
            dt_split = ["No Date", "00"]
        return dt_split

    @staticmethod
    def get_dimensions(f):
        return "{0}{1}{2}".format(Image.open(f)._getexif()[40962], "x",Image.open(f)._getexif()[40963])