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

from app import Rules


class ImageUtils:

    @staticmethod
    def get_dt_captured(filename):
        # Check to see if it is even a file and then begin
        if os.path.isfile(filename):
            try:
                # First method uses exif and works mainly for images
                exif = Image.open(filename)._getexif().items()
                dt = ImageUtils.get_exif_field(filename, exif, 'DateTimeOriginal')

                if dt is not "NotFound" and dt is not None:
                    return dt

            except Exception as err:
                if Rules.get_debug() is True:
                    print("get_dt_captured(): Metadata extraction error: %s" % err)

            # If the date wasn't found or didn't exist, try a different approach
            dt = ImageUtils.get_alt_metadata(filename)
            if dt is not None:
                return dt
            else:
                # Everything failed, so date doesn't exist
                return "0000:00:00 00:00:00"

    @staticmethod
    def get_exif_field(fn, exif, field):
        # First attempt to get by fieldname
        for (k, v) in exif:
            # print('%s = %s' % (TAGS.get(k), v))
            key_name = TAGS.get(k)
            if key_name == field:
                return v

        try:
            # Second attempt is to get by index
            dt = Image.open(fn)._getexif()[36867]
            if dt is not None and dt is not "":
                return dt
        except Exception as err:
            # Finally, admit not found
            return "NotFound"

    @staticmethod
    def get_alt_metadata(filename):
        # First create a parser
        parser = createParser(filename)
        if not parser:
            if Rules.get_debug() is True:
                print("Unable to parse file")
            return None

        # If the parse worked, try extracting Metadata
        try:
            metadata = extractMetadata(parser)
        except Exception as err:
            if Rules.get_debug() is True:
                print("Metadata extraction error: %s" % err)
            return None

        if not metadata:
            if Rules.get_debug() is True:
                print("Unable to extract metadata")
            return None

        metatext = metadata.exportPlaintext()

        # Check metadata to find a date
        if Rules.get_debug() is True:
            print("Printing Metadata")
        for line in metatext:
            if "- Creation date: " in line:
                return line.replace("- Creation date: ", "")

        # Parse metadata failed. Last hope so returning None
        return None

    @staticmethod
    def get_dt_captured_split(str_dt="0000:00:00 00:00:00"):

        try:
            # First split on any spaces
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
        except ValueError as err:
            print("Not a valid YYYY:MM:DD date pattern.")
            return err
        except Exception as err:
            print("Unknown error has occurred: {0}".format(err))
            return err

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
