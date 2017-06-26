# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch
import os

from app import FileUtils
from app import ImageUtils
from app import Rules

# STR_DIR = r"/Users/paulottley/Desktop/SortSource"
STR_DIR = r"/Volumes/Elements2TB/Backups/Pictures/images"

TGT_DIR = r"/Volumes/MyBook2TB/Backups/SortTarget"

for root, dirs, files in os.walk(STR_DIR):
    for file in files:

        target_dir = root

        tgt_folder = FileUtils.get_file_category(file)

        try:
            dt, str_dt = ImageUtils.get_dt_from_name(file)
            if dt is None:
                print("Zero or None: " + file)
                target_dir = "{0}{1}{2}{3}".format(
                                                    root,
                                                    os.sep,
                                                    "no_date",
                                                    os.sep)
            else:
                target_dir = "{0}{1}{2}{3}{4}{5}".format(
                                                    root + os.sep,
                                                    tgt_folder + os.sep,
                                                    dt.year,
                                                    os.sep,
                                                    dt.month,
                                                    os.sep)

            FileUtils.move_file(root + os.sep + file, target_dir, file)

        except Exception as err:
            print("Date failed on: {0} with error: {1}".format(file, err))


