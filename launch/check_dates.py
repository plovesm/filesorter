# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch

from app import NavUtil

STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/dv"

all_files1 = NavUtil.walk_dir(STR_DIR1, STR_DIR1)

# Check date of original file

# Parse date

# Find mp4 file of same name

# Update date

for file in all_files1:
    print("Filename: {0} date: {1}".format(file.get_filename(), file.get_date_taken()))