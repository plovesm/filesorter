# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter program

from app import FileSorter

STR_DIR1 = r"/Volumes/Elements2TB/OttleyFamilyShare/FamilyShare.photoslibrary/Masters"
STR_DIR15 = r"smb://Paul’s iMac._smb._tcp.local/Elements2TB/OttleyFamilyShare/FamilyShare.photoslibrary/Masters"
STR_DIR2 = r"/Volumes/MyBook2TB/Backups/Pictures"
STR_DIR25 = r"/Volumes/MyBook2TB/Backups/SortTarget"
STR_DIR3 = r"/Users/paulottley/Desktop/MomsDadsPhotos"

TGT_DIR1 = r"/Volumes/Elements2TB/SortTarget"

fs = FileSorter(STR_DIR1, TGT_DIR1)
# fs.start_up()

all_files1 = fs.walk_dir(STR_DIR15, TGT_DIR1)
# all_files2 = fs.walk_dir(STR_DIR25, TGT_DIR1)

# file_lists = fs.merge_files(all_files1, all_files2)

file_lists = fs.mark_duplicates(all_files1)

fs.final_report(file_lists)

