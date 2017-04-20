# @author Paul Ottley
# @copyright 2017

import re

from app import NavUtil


STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/3gp"

all_files1 = NavUtil.walk_dir(STR_DIR1, STR_DIR1)

# Check date of original file

# Parse date

# Find mp4 file of same name

# Update date

regex = re.compile(r'20\d{2}')  # /(20\d{6})|(20\d{2}-\d{2}-\d{2})/g')

for file in all_files1:
    m = re.search(r'\d{4}-\d{2}-\d{2}', file.get_filename())  # regex.match(file.get_filename())
    dtfrmname = ""
    if m is not None:
        dtfrmname = m.group()

    print("Filename: {0} date: {1} filename_date: {2}".format(file.get_filename(),
                                                              file.get_date_taken(),
                                                              dtfrmname))