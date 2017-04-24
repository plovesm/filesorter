# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch
import os
import re
from shutil import move

STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library"
STR_DIR2 = r"/Volumes/MyBook2TB/Backups/SortTarget"
STR_DIR3 = r"/Volumes/MyBook2TB/Backups/Library"

count = 0

for root, dirs, files in os.walk(STR_DIR1):
    for file in files:
        m = re.search(r'(20\d{2}\d{2}\d{2}-)', file)
        if m is not None:
            print(file)
        # move(root + os.sep + file, STR_DIR1 + os.sep + file)
        count += 1

print(count)
