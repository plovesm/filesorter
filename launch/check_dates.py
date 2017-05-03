# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch
import os
import platform
import datetime, time

from app import NavUtil

# STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/m4v"
STR_DIR1 = r"/Users/paulottley/Desktop/SortSource"

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

    if platform.system() == 'Windows':
        creation_date = os.path.getctime(file.get_full_path())
    else:
        stat = os.stat(file.get_full_path())
        try:
            creation_date = stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            creation_date = file.get_date_taken()
    # creation_date_str = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(creation_date))
    dt = datetime.date.fromtimestamp(creation_date)

    # dt = datetime.date.fromordinal(creation_date)
    creation_date_str = "{0}:{1}:{2} 00:00:00".format(dt.year, dt.month, dt.day)
    # print("Created: %s" % time.ctime(os.path.getctime(file.get_full_path())))

    print("Filename: {0} date: {1}".format(file.get_filename(), creation_date_str))

print("Total count: {0} Zero Count: {1}".format(count, zero_count))
