# @author Paul Ottley
# @copyright 2017

import re

from app import FileUtils
from app import ImageUtils
from app import NavUtil


STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/wmv"
STR_DIR2 = r"/Users/paulottley/Desktop/SortSource"

all_files1 = NavUtil.walk_dir(STR_DIR1, STR_DIR1)

# Check date of original file

# Parse date

# Find mp4 file of same name

# Update date

for file in all_files1:
    print("Before Filename: {0} date: {1} filename parser date: {2}".format(file.get_filename(),
                                                                            file.get_date_taken(),
                                                                            ImageUtils.get_dt_from_parser(
                                                                                file.get_full_path())))

    file_type = FileUtils.get_file_type(file.get_filename())
    date = ImageUtils.get_original_date(file.get_full_path())
    if file_type == "mp4":
        dt = ImageUtils.get_dt_captured_split(date)
        ImageUtils.set_date(file.get_full_path(), dt.year, dt.month, dt.day)

    print("After Filename: {0} date: {1} filename parser date: {2}".format(file.get_filename(),
                                                                           file.get_date_taken(),
                                                                           ImageUtils.get_dt_from_parser(
                                                                               file.get_full_path())))
