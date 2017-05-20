# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch
import os
import platform
import datetime, time

from app import FileUtils
from app import ImageUtils
from app import NavUtil
STR_DIR1 = r"/Volumes/Elements2TB/Backups/Library/Embed_fail_new"
# STR_DIR1 = r"/Users/paulottley/Desktop/SortSource"
# STR_DIR1 = r"/Volumes/Macintosh HD-1/Users/paulottley/Movies/iMovie Library.imovielibrary/5-1-17/Original Media"
# STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Videos/iMovie Library.imovielibrary/My Movie/Original Media"

all_files1 = NavUtil.walk_dir(STR_DIR1, STR_DIR1)

# Check date of original file

# Parse date

# Find mp4 file of same name

# Update date
count = 0
zero_count = 0
for file in all_files1:
    count += 1
    if "0000:00:00 00:00:00" == file.get_date_taken():
        zero_count += 1
    """

    dt = ImageUtils.get_dt_created_from_file(file)
    month = str(dt.month)
    if dt.month < 10:
        month = "0" + month

    day = str(dt.day)
    if dt.day < 10:
        day = "0" + day

    creation_date_str = "{0}-{1}-{2}".format(dt.year, month, day)
    """
    full_filename = file.get_full_path()
    filename = file.get_filename()

    new_file = file.get_filename().replace("_.", ".")  # "_{0}_".format(creation_date_str))
    new_file = new_file.replace("....", ".")  # "_{0}_".format(creation_date_str))
    if FileUtils.does_file_exist(new_file, file.get_src_dir()) is not True:
        print(file.get_src_dir() + new_file)
        os.rename(file.get_full_path(), file.get_src_dir() + new_file)
    else:
        print(new_file + " file exists")

    if "." is filename[0]:
        print("Moving..." + full_filename)
        FileUtils.move_file(full_filename, r"/Volumes/Elements2TB/Backups/Trash/", filename)


    print("Filename: {0} date: {1}".format(file.get_filename(), file.get_date_taken()))  # creation_date_str))

print("Total count: {0} Zero Count: {1}".format(count, zero_count))
