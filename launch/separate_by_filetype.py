# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch
import os

from app import FileUtils

STR_DIR3 = r"/Volumes/MyBook2TB/Backups/Library"
STR_DIR4 = r"/Users/paulottley/Google Drive/MomsDadsPhotos"

TGT_DIR1 = r"/Users/paulottley/Desktop/SortTarget"

for root, dirs, files in os.walk(STR_DIR3):
    for file in files:
        ext = FileUtils.get_file_type(file)
        FileUtils.move_file(root + os.sep + file, STR_DIR3 + os.sep + ext + os.sep, file)

# Step 1 Walk the directory

# Step 2 Determine filetype by extension

# Step 3 Move to appropriate folder