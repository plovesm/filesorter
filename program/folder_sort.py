# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter program

from app import FileSorter


STR_DIR1 = r"/Users/paulottley/Google Drive/MomsDadsPhotos"

TGT_DIR1 = r"/Users/paulottley/Desktop/SortTarget"

fs = FileSorter(STR_DIR1, TGT_DIR1)

all_files1 = fs.walk_dir(STR_DIR1, TGT_DIR1)

file_lists = fs.mark_duplicates(all_files1)

fs.copy_files(file_lists[0])

fs.final_report(file_lists)
