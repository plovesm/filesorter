# @author Paul Ottley
# @copyright 2017

import re

from app import FileUtils, Rules, ImageUtils, NavUtil


STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/mpg"
STR_DIR2 = r"/Users/paulottley/Desktop/SortSource"

all_files1 = NavUtil.walk_dir(STR_DIR2, STR_DIR2)

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
    """
    if file_type != "mp4" and file.get_type() != Rules.get_oth_tag():
        full_path = file.get_full_path()
        mp4_full_path = full_path.replace("." + file_type, ".mp4")
        # mp4_full_path = full_path.replace("." + file_type.swapcase(), ".mp4")
        print("Date: {0} Filename: {1}".format(date, mp4_full_path))
    """
    dt = ImageUtils.get_dt_captured_split(date)
    ImageUtils.set_date(file.get_full_path(), dt.year, dt.month, dt.day)

    print("After Filename: {0} date: {1} filename parser date: {2}".format(file.get_filename(),
                                                                           file.get_date_taken(),
                                                                           ImageUtils.get_dt_from_parser(
                                                                               file.get_full_path())))
