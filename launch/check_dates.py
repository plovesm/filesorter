# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch
import os
import re

from app import FileUtils
from app import ImageUtils
from app import NavUtil

# STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/m4v"
# STR_DIR1 = r"/Users/paulottley/Desktop/SortSource"
# STR_DIR1 = r"/Volumes/Macintosh HD/Users/paulottley/Movies/iMovie Library.imovielibrary/5-1-17/Original Media"
# STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/videos/Cleanup"
STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/Cleanup"

all_files1 = NavUtil.walk_dir(STR_DIR1, STR_DIR1)

# Check date of original file

# Parse date

# Find mp4 file of same name

# Update date
count = 0
zero_count = 0
missing_filename_dt = 0
for file in all_files1:
    count += 1
    tgt_dir = file.get_tgt_dir()
    if "0000:00:00 00:00:00" == file.get_date_taken() or "2000:01:01 00:00:00" == file.get_date_taken():
        zero_count += 1
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        # FileUtils.move_file(file.get_full_path(), tgt_dir + "Cleanup/", file.get_tgt_filename())

    m = re.search(r"(19|20)\d\d[- /.:_]?(1[012]|0?[1-9])[- /.:_]?([12][0-9]|3[01]|0?[1-9])", file.get_filename())

    # Pull full date from name
    if m is None:
        missing_filename_dt += 1
        print("***********************")
        # FileUtils.move_file(file.get_full_path(), "Cleanup/", file.get_tgt_filename())
    else:
        # Set the date from the filename and move it out of cleanup
        file_type = FileUtils.get_file_type(file.get_filename())
        date = ImageUtils.get_original_date(file.get_full_path())
        dt = ImageUtils.get_dt_captured_split(date)
        ImageUtils.set_date(file.get_full_path(), dt.year, dt.month, dt.day)
        # Move it out of Cleanup
        if "Cleanup/" in tgt_dir:
            tgt_dir = tgt_dir.replace("Cleanup/", "")

        FileUtils.move_file(file.get_full_path(), tgt_dir, file.get_tgt_filename())
    print("Filename: {0} date: {1}".format(file.get_filename(), file.get_date_taken()))

print("Total count: {0} Zero Count: {1} Missing date in filename: {2}".format(count, zero_count, missing_filename_dt))
