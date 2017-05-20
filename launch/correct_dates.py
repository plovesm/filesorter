# @author Paul Ottley
# @copyright 2017

import re

from app import FileUtils, Rules, ImageUtils, NavUtil


# STR_DIR1 = r"/Volumes/Macintosh HD-1/Users/paulottley/Movies/iMovie Library.imovielibrary/5-1-17/Original Media"
# STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Videos/iMovie Library.imovielibrary/My Movie/Original Media"
STR_DIR1 = r"/Volumes/Elements2TB/Backups/Library/Embed_fail_new"
STR_DIR2 = r"/Users/paulottley/Desktop/SortSource"

all_files1 = NavUtil.walk_dir(STR_DIR1, STR_DIR1)

# Check date of original file

# Parse date

# Find mp4 file of same name

# Update date

for file in all_files1:
    print("Before Filename: {0} date: {1} filename parser date: {2}".format(
        file.get_filename(),
        file.get_date_taken(),
        ImageUtils.get_dt_from_parser(file.get_full_path())))

    file_type = FileUtils.get_file_type(file.get_filename())
    date = ImageUtils.get_dt_from_name(file.get_filename())
    """
    if file_type != "mp4" and file.get_type() != Rules.get_oth_tag():
        full_path = file.get_full_path()
        mp4_full_path = full_path.replace("." + file_type, ".mp4")
        # mp4_full_path = full_path.replace("." + file_type.swapcase(), ".mp4")
        print("Date: {0} Filename: {1}".format(date, mp4_full_path))
    """
    full_filename = file.get_full_path()
    pdate = ImageUtils.get_dt_from_parser(file.get_full_path())
    dt = ImageUtils.get_dt_captured_split(date)
    if int(pdate[:4]) != int(date[:4]):
        ImageUtils.set_date(file.get_full_path(), date, dt.year, dt.month, dt.day)
        # print("Moving..." + full_filename)
        # FileUtils.move_file(full_filename, r"/Volumes/Elements2TB/Backups/Library/Date_Error/", file.get_filename())

        print("After Filename: {0} date: {1} filename parser date: {2}".format(
            file.get_filename(),
            file.get_date_taken(),
            ImageUtils.get_dt_from_parser(file.get_full_path())))
