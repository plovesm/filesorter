# ImageUtils
# @author Paul Ottley
# @copyright 2017
import os
import datetime

from app import Mov
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
                    print("No date found. Trying different method.")
                    dt = ImageUtils.get_alt_metadata2(f)
                    # dt = Image.open(f)._getexif()[36867]
            except Exception as err:
                print("get_dt_captured(): Metadata extraction error: %s" % err)
                dt = ImageUtils.get_alt_metadata(f)

        return dt

    @staticmethod
    def get_alt_metadata(f):
        dt = "0B:00:00"
        try:
            parser = createParser(f)
            if not parser:
                print("Unable to parse file")
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
                print("Unable to extract metadata")
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
            print("Unable to parse file")
        try:
            metadata = extractMetadata(parser)
        except Exception as err:
            print("Metadata extraction error: %s" % err)
            metadata = None
        if not metadata:
            print("Unable to extract metadata")

        text = metadata.exportPlaintext()

        for line in text:
            print(line)

        return metadata

    @staticmethod
    def get_dt_captured_split(str_dt="0000:00:00 00:00:00"):
        print("Date recieved: {0} len: {1}".format(str_dt, len(str_dt.split())))

        dt = str_dt.split()[0]

        # Go through date and extract year, month
        if dt is not None:
            if "-" in dt:
                dt = dt.replace("-", ":")
            else:
                print("Check date: {0}".format(str_dt))

        # Convert to date
        d = datetime.datetime.strptime(dt, "%Y:%m:%d")

        # Return the date as a date object
        return d

    @staticmethod
    def get_dimensions(f):
        return "{0}{1}{2}".format(Image.open(f)._getexif()[40962], "x",Image.open(f)._getexif()[40963])

    @staticmethod
    def set_date(fn, year, month, day):
        try:
            dt = datetime.date(year, month, day)
            strdt = dt.strftime("%Y-%m-%d %H:%M:%S")

            m = Mov(fn)
            m.parse()

            if strdt is not "":
                d = datetime.datetime.strptime(strdt, "%Y-%m-%d %H:%M:%S")
                m.set_date(d)
        except Exception as err:
            print("Setting date failed: " + err)
