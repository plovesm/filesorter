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
from app import FileUtils

CURRENT_YEAR = datetime.datetime.now().year


class ImageUtils:

    @staticmethod
    def get_original_date(filename, deep=False):

        date_frm_filename = None
        date_frm_exif_data = None  # Images Only
        date_frm_atom = None  # Video Only
        date_frm_parser = None  # Images or Videos

        path, fn = os.path.split(filename)
        file_category = FileUtils.get_file_category(fn)

        # First, see if there is a date in the filename (Easiest and universal)
        dt_frm_file, str_dt_frm_file = ImageUtils.get_dt_from_name(fn)
        if dt_frm_file is not None and str_dt_frm_file is not None:
            date_frm_filename = dt_frm_file

        # Next, pull a date from the metadata
        if os.path.isfile(filename):
            if file_category == Rules.get_img_dir():
                try:
                    # First method uses exif and works mainly for images
                    exif = Image.open(filename)._getexif().items()
                    dt = ImageUtils.get_exif_field(filename,
                                                   exif,
                                                   'DateTimeOriginal')

                    if dt is not "NotFound" and dt is not None:
                        date_frm_exif_data = re.sub(r"\D", "", dt.split(" ")[0])

                except Exception as err:
                    if Rules.get_debug() is True:
                        print("get_original_date(): Metadata extraction error: %s" % err)

            elif file_category == Rules.get_vid_dir():
                # First, try Atom Parser
                if deep is True and os.path.isfile(filename):
                    dt_from_atom = ImageUtils.get_dt_from_atom_parser(filename)
                    if dt_from_atom is not None and \
                            "0000" not in dt_from_atom and \
                            CURRENT_YEAR >= int(dt_from_atom[:4]) > 1970:
                        date_frm_atom = re.sub(r"\D", "", dt_from_atom.split(" ")[0])

            elif date_frm_exif_data is None and date_frm_atom is None:
                    dt = ImageUtils.get_dt_from_parser(filename)
                    if dt is not None:
                        date_frm_parser = re.sub(r"\D", "", dt.split(" ")[0])

        else:
            print("Not a file: " + str(filename))
            return None, None

        # Finally, compare the two for the most likely one
            # Earliest date
            # After 1970
            # Not past the current year

        date_list = [date_frm_filename,
                     date_frm_exif_data,
                     date_frm_atom,
                     date_frm_parser]

        best_date_taken = ImageUtils.get_earliest_date(date_list)

        return ImageUtils.get_date_obj(best_date_taken)  # Date object and string (YYYY-MM-DD)

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
            # We start with a container to hold ALL the dates found in the name
            date_list = []

            # Make a copy of the name to check against
            filename_chk = filename

            # Check numeric date matches (ie. 2017-06-13)
            while re.search(Rules.get_date_regex(), filename_chk):
                m = re.search(Rules.get_date_regex(), filename_chk)
                found_date = re.sub(r"\D", "", m.group())

                if CURRENT_YEAR >= int(found_date[:4]) > Rules.get_oldest_year():
                    date_list.append(found_date)

                filename_chk = filename_chk.replace(m.group(), "")

            # Check for dates with letters (ie. Apr 14, 2017)
            while re.search(Rules.get_date_regex_word(), filename_chk):
                m = re.search(Rules.get_date_regex_word(), filename_chk)
                date_word = m.group()
                filename_chk = filename_chk.replace(m.group(), "")

                month = Rules.get_months_list()[date_word[:3]]
                year = date_word[(len(date_word)-4):]

                if len(date_word) == 12:
                    day = date_word[4] + date_word[4]
                else:
                    day = "0" + date_word[4]

                date_list.append(year + month + day)

            # Iterate through the list and find the earliest date within boundaries
            dt_frm_name = ImageUtils.get_earliest_date(date_list)

            if dt_frm_name is None:
                # Short circuit and return None
                return None, None

            # Return String formatted (YYYY-MM-DD) and Date obj
            return ImageUtils.get_date_obj(dt_frm_name)

        # It wasn't even a string to begin with
        return None, None

    @staticmethod
    def get_earliest_date(date_list):
        dt_frm_name = None
        if date_list is not None and len(date_list) > 0:
            dt_frm_name = date_list[0]
            # Find the oldest date that is over 1970
            if len(date_list) > 1:
                for date in date_list:
                    date_chk = date
                    if date_chk is not None and (
                                    dt_frm_name is None or (
                                            int(date_chk) < int(dt_frm_name) and
                                            int(dt_frm_name[:4]) - int(date_chk[:4]) < 10)):
                        # Make sure it is a valid date
                        try:
                            dt = datetime.datetime.strptime(date_chk, "%Y%m%d")
                            dt_frm_name = date_chk
                        except Exception as err:
                            print("Not valid date: " + str(err))

        return dt_frm_name

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

    @classmethod
    def get_date_obj(cls, stripped_date):

        # Now convert date string to date object
        try:

            dt = datetime.datetime.strptime(stripped_date, "%Y%m%d")

            dt_frm_name_year = str(dt.year)
            dt_frm_name_month = str(dt.month)
            dt_frm_name_day = str(dt.day)

        except Exception:
            # If anything went wrong, remove from list then try again
            print("Unable to parse date")
            return None, None

        # add leading zeros if needed
        if len(dt_frm_name_month) is 1:
            dt_frm_name_month = "0" + dt_frm_name_month

        if len(dt_frm_name_day) is 1:
            dt_frm_name_day = "0" + dt_frm_name_day

        formatted_dt = "{0}-{1}-{2}".format(dt_frm_name_year,
                                            dt_frm_name_month,
                                            dt_frm_name_day)

        return formatted_dt, dt
