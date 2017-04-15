# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch
import os
from shutil import move

from app import FileSorter

STR_DIR1 = r"/Users/paulottley/Movies/iMovie Library.imovielibrary/4-2-17/Original Media"
STR_DIR2 = r"/Volumes/OttFamilyShare/Backups/Library/To be imported"
STR_DIR3 = r"/Volumes/MyBook2TB/Backups/Library"

TGT_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/videos"

for root, dirs, files in os.walk(STR_DIR3):
    for file in files:
        if "to_import_" in file:
            new_file = file.replace("to_import_", "")
            print(root + os.sep + new_file)
            os.rename(root + os.sep + file, root + os.sep + new_file)

"""
fs = FileSorter(STR_DIR2, STR_DIR2)

all_files1 = fs.walk_dir(STR_DIR2, STR_DIR2)

file_lists = [all_files1, []]  # fs.mark_duplicates(all_files1)

for x in file_lists[0]:
    filename_arr = x.get_tgt_filename().rpartition("To be imported_")
    x.set_tgt_filename(filename_arr[2])

fs.move_files(file_lists[0])

fs.final_report(file_lists)
"""