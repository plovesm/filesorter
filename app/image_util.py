# ImageUtils
# @author Paul Ottley
# @copyright 2017
import os
import datetime
import platform
import re

from app import Mov
from PIL import Image
from PIL.ExifTags import TAGS
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

from app import Rules

CURRENT_YEAR = datetime.datetime.now().year


class ImageUtils:

    @staticmethod
    def get_original_date(filename, deep=False):

        # First, try Atom Parser
        if deep is True and os.path.isfile(filename):
            dt_from_atom = ImageUtils.get_dt_from_atom_parser(filename)
            if dt_from_atom is not None and \
                    "0000" not in dt_from_atom and \
                    CURRENT_YEAR >= int(dt_from_atom[:4]) > 1970:
                return dt_from_atom

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
                    print("get_original_date(): Metadata extraction error: %s" % err)

            # If the date wasn't found or didn't exist, try a different approach
            dt = ImageUtils.get_dt_from_parser(filename)
            if dt is not None:
                return dt

            # Next, see if the date is found in the filename
            path, fn = os.path.split(filename)
            dt_from_file = ImageUtils.get_dt_from_name(fn)
            if dt_from_file is not None and CURRENT_YEAR >= int(dt_from_file[:4]) > 1970:
                return dt_from_file
            else:
                # Everything failed, so date doesn't exist
                return "0000-00-00 00:00:00"

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
            elif "- Creation time: " in line:
                return line.replace("- Creation time: ", "")
        # Last hope so returning None
        return None

    @staticmethod
    def get_dt_from_atom_parser(filename=""):
        fn = filename
        # noinspection PyBroadException
        try:
            m = Mov(fn)
            original_date = m.parse()

            return original_date
        except Exception as err:
            if Rules.get_debug() is True:

                print(filename + " Atom Parser failed...")
            return None

    @staticmethod
    def get_dt_from_name(filename=""):
        if isinstance(filename, str):
            dt_frm_name = ""
            dt_frm_name_month = ""
            dt_frm_name_day = ""

            date_list = []

            filename_chk = filename

            while re.search(Rules.get_date_regex(), filename_chk):
                m = re.search(Rules.get_date_regex(), filename_chk)
                date_list.append(m.group())
                filename_chk = filename_chk.replace(m.group(), "")

            while re.search(Rules.get_date_regex_word(), filename_chk):
                m = re.search(Rules.get_date_regex_word(), filename_chk)
                date_word = m.group()
                filename_chk = filename_chk.replace(m.group(), "")

                month = Rules.get_months_list()[date_word[:3]]
                year = date_word[(len(date_word)-4):]
                day = "01"

                if len(date_word) == 12:
                    day = date_word[4] + date_word[4]
                else:
                    day = "0" + date_word[4]

                date_list.append(year + month + day)

            # Pull full date from name
            if date_list is not None and len(date_list) > 0:
                dt_frm_name = re.sub(r"\D", "", date_list[0])
                # Find the oldest date

                if len(date_list) > 1:
                    for date in date_list:
                        date_chk = re.sub(r"\D", "", date)
                        if int(date_chk) < int(dt_frm_name):
                            dt_frm_name = date_chk

            try:

                dt = datetime.datetime.strptime(dt_frm_name, "%Y%m%d")

                dt_frm_name_month = str(dt.month)
                dt_frm_name_day = str(dt.day)

            except Exception:
                print("Unable to parse date for " + filename)

            full_dt_frm_name = dt_frm_name

            # add leading zeros if needed
            if len(dt_frm_name_month) is 1:
                dt_frm_name_month = "0" + dt_frm_name_month

            if len(dt_frm_name_day) is 1:
                dt_frm_name_day = "0" + dt_frm_name_day

            # If I had to parse out the month and day then build it back
            if len(dt_frm_name_month) is 2 and len(dt_frm_name_day) is 2:
                full_dt_frm_name = dt_frm_name[:4] + dt_frm_name_month + dt_frm_name_day

            stripped_dt = re.sub(r'\D', "", full_dt_frm_name)
            if len(stripped_dt) is 8:
                formatted_dt = stripped_dt[:4] + "-" + stripped_dt[4:]
                formatted_dt = formatted_dt[:7] + "-" + formatted_dt[7:]
                return formatted_dt + " 00:00:00"

            # It's all or nothing
            return None
        return None

    @staticmethod
    def get_dt_created_from_file(file):
        if platform.system() == 'Windows':
            creation_date = os.path.getctime(file.get_full_path())
        else:
            stat = os.stat(file.get_full_path())
            try:
                creation_date = stat.st_birthtime
            except AttributeError:
                # We're probably on Linux. No easy way to get creation dates here,
                # so we'll settle for when its content was last modified.
                creation_date = file.get_date_taken()

        if "-" in str(creation_date) or ":" in str(creation_date):
            dt = ImageUtils.get_dt_captured_split(creation_date)
        else:
            dt = datetime.date.fromtimestamp(creation_date)

        return dt

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
            dt = datetime.datetime.strptime(dt, "%Y:%m:%d")
            if dt is not None:
                month = str(dt.month)
                if dt.month < 10:
                    month = "0" + month

                day = str(dt.day)
                if dt.day < 10:
                    day = "0" + day

                year = str(dt.year)

                # Return the date as a date object
                return year, month, day, dt

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
    def set_date(fn, str_dt="", year=1950, month=1, day=1, output=False):
        try:
            if str_dt is "":
                dt = datetime.date(year, month, day)
                str_dt = dt.strftime("%Y-%m-%d %H:%M:%S")

            m = Mov(fn)
            m.parse(output)

            if str_dt is not "":
                d = datetime.datetime.strptime(str_dt, "%Y-%m-%d %H:%M:%S")
                m.set_date(d)
        except Exception as err:
            print("Setting date failed: {0}".format(err))
            # See if it is an image and try updating Exif
            """
            try:
                img = pexif.JpegFile.fromFile(fn)

                # Get the orientation if it exists
                image_tags = img.exif.primary.tags
                # img.exif.primary.Orientation = [1]
                # img.writeFile(fn)
                print(image_tags)
            except Exception as err:
                print("Image dates didn't work: " + err)
            """