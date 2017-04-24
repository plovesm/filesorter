# ImageUtils
# @author Paul Ottley
# @copyright 2017
import os
import datetime
import re

from app import Mov
from PIL import Image
from PIL.ExifTags import TAGS
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

from app import Rules


class ImageUtils:

    @staticmethod
    def get_original_date(filename):
        # First, see if the date is found in the filename
        dt_from_file = ImageUtils.get_dt_from_name(filename)
        if dt_from_file is not None:
            return dt_from_file

        # Next, check to see if it is even a file and then begin
        if os.path.isfile(filename):
            try:
                # First method uses exif and works mainly for images
                exif = Image.open(filename)._getexif().items()
                dt = ImageUtils.get_exif_field(filename, exif, 'DateTimeOriginal')

                if dt is not "NotFound" and dt is not None:
                    return dt

            except Exception as err:
                if Rules.get_debug() is True:
                    print("get_original_date(): Metadata extraction error: %s" % err)

            # If the date wasn't found or didn't exist, try a different approach
            dt = ImageUtils.get_dt_from_parser(filename)
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
    def get_dt_from_parser(filename):
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

        # Last hope so returning None
        return None

    @staticmethod
    def get_dt_from_name(filename=""):
        if isinstance(filename, str):
            # m = re.search(r'([12][09]\d{2}[-:.]\d{2}[-:.]\d{2})|([12][09]\d{2}\d{2}\d{2})', filename)
            m = re.search(r'(20\d{2}[-:._]\d{2}[-:._]\d{2})|'
                          r'(19\d{2}[-:._]\d{2}[-:._]\d{2})|'
                          r'(20\d{2}\d{2}\d{2})|'
                          r'(19\d{2}\d{2}\d{2})', filename)
            dt_frm_name = ""

            if m is not None:
                dt_frm_name = m.group()

            stripped_dt = re.sub(r'\D', "", dt_frm_name)

            if len(stripped_dt) is 8:
                formatted_dt = stripped_dt[:4] + ":" + stripped_dt[4:]
                formatted_dt2 = formatted_dt[:7] + ":" + formatted_dt[7:]
                return formatted_dt2 + " 00:00:00"

            # It's all or nothing
            return None
        return None

    @staticmethod
    def get_dt_captured_split(str_dt="0000:00:00 00:00:00"):

        try:
            # First split on any spaces
            dt = str_dt.split(" ")[0]

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
            return datetime.datetime.strptime("2000:01:01", "%Y:%m:%d")
        except Exception as err:
            print("Unknown error has occurred: {0}".format(err))
            return datetime.datetime.strptime("2000:02:02", "%Y:%m:%d")

    @staticmethod
    def get_dimensions(f):
        return "{0}{1}{2}".format(Image.open(f)._getexif()[40962], "x",Image.open(f)._getexif()[40963])

    @staticmethod
    def remove_false_datestamp(filename):
        file = filename
        m = re.search(r'^(20\d{2}\d{2}\d{2}-)', file)
        if m is not None:
            new_file = file.replace(m.group(), "")

            print(new_file)
            if file != new_file:
                file = new_file

        return file

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
            print("Setting date failed: {0}".format(err))
