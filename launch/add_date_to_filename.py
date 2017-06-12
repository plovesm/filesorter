# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch
import os
import platform
import datetime, time

from app import FileUtils
from app import ImageUtils
from app import NavUtil
STR_DIR1 = r"/Volumes/Elements2TB/Backups/Pictures/images"
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
    full_filename = file.get_full_path()
    path, fn = os.path.split(full_filename)
    date_taken = file.get_date_taken()

    if "0000" in date_taken:
        zero_count += 1

    year, month, day, dt = ImageUtils.get_dt_captured_split()

    creation_date_str = "{0}-{1}-{2}".format(year, month, day)

    new_file = fn.replace("images_", "")
    new_file = new_file.replace("_.", ".")
    new_file = new_file.replace("....", ".")
    new_file = "{0}_{1}".format(creation_date_str, fn)
    if FileUtils.does_file_exist(new_file, path) is not True:
        print(path + new_file)
        os.rename(full_filename, path + new_file)
    else:
        print(new_file + " file exists")

    print("Filename: {0} date: {1}".format(fn, date_taken))

print("Total count: {0} Zero Count: {1}".format(count, zero_count))
