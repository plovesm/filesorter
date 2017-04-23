# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch

from app import NavUtil

STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/jpg"
STR_DIR2 = r"/Users/paulottley/Desktop/SortSource"

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

    print("Filename: {0} date: {1}".format(file.get_filename(), file.get_date_taken()))

print("Total count: {0} Zero Count: {1}".format(count, zero_count))
