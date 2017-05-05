# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch
import os

from app import NavUtil

# STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/m4v"
# STR_DIR1 = r"/Users/paulottley/Desktop/SortSource"
STR_DIR1 = r"/Volumes/Macintosh HD/Users/paulottley/Movies/iMovie Library.imovielibrary/5-1-17/Original Media"

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
    if "Clip_" in file.get_filename():
        new_file = file.get_filename().replace("Clip_", "VidArch_")
        print(file.get_src_dir() + new_file)
        os.rename(file.get_full_path(), file.get_src_dir() + new_file)
    """
    print("Filename: {0} date: {1}".format(file.get_filename(), file.get_date_taken()))

print("Total count: {0} Zero Count: {1}".format(count, zero_count))
