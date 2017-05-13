# @author Paul Ottley
# @copyright 2017


import os
import re

from app import FileUtils
from app import ImageUtils

count = 0
zero_count = 0

STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library"
# STR_DIR1 = r"/Users/paulottley/Desktop/Botched"
index = 0
for root, dirs, files in os.walk(STR_DIR1):
    for file in files:
        full_filename = root + os.sep + file
        orig_datetime = ImageUtils.get_original_date(full_filename)
        orig_date = orig_datetime.split(" ")[0]
        new_file = file

        if "0000" in orig_date or "2000" in orig_date:
            if file[0] is not ".":
                zero_count += 1

                # print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("0000000 Filename: {0} date: {1}".format(file, orig_date))

        # First, set the date so it is consistent
        # ImageUtils.set_date(full_filename, orig_datetime)
fc\
        # Next, Clean up the name,
        #  - remove all spaces
        #  - check if there is a date mismatch with filename and take earliest
        #  - remove oddly formatted dates in the filename
        #  - Rename file to have consistent date pattern on the beginning

        new_file = new_file.replace(" ", "_")

        print("File: {0} Date: {1}".format(file, orig_datetime))

        m = re.search(r"(19|20)\d\d[- /.:_]?(1[012]|0?[1-9])[- /.:_]?([12][0-9]|3[01]|0?[1-9])[- /:_]?", file)

        if None is not m and None is not m.group():
            date_frm_filename = m.group()
            new_file = new_file.replace(date_frm_filename,"")

        new_file = orig_date + "_" + new_file

        while FileUtils.does_file_exist(new_file, root + os.sep) is True:
            print("Dup: " + new_file)
            new_file = FileUtils.add_suffix(new_file, "1")

        full_new_file = root + os.sep + new_file

        # os.rename(full_filename, full_new_file)
        print(full_new_file)

        index += 1
