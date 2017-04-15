# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch

from app import NavUtil


STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/videos"
STR_DIR2 = r"/Volumes/OttFamilyShare-3/Backups/Library/To be imported"

TGT_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/videos"

fs = NavUtil(STR_DIR2, STR_DIR2)

all_files1 = fs.walk_dir(STR_DIR2, STR_DIR2)

file_lists = [all_files1, []]  # fs.mark_duplicates(all_files1)

fs.move_files(file_lists[0])

fs.final_report(file_lists)
