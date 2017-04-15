# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch


from app import FileSorter

STR_DIR1 = r"/Users/paulottley/Movies/iMovie Library.imovielibrary/4-2-17/Original Media"
STR_DIR2 = r"/Volumes/OttFamilyShare/Backups/Pictures"
STR_DIR3 = r"/Volumes/MyBook2TB/Backups/Library/wmv"
STR_DIR4 = r"/Users/paulottley/Google Drive/MomsDadsPhotos"

TGT_DIR1 = r"/Users/paulottley/Desktop/SortTarget"

fs = FileSorter(STR_DIR4, TGT_DIR1)

all_files1 = fs.walk_dir(STR_DIR4, TGT_DIR1)

file_lists = [all_files1, []]

fs.move_files(file_lists[0])

# fs.final_report(file_lists)

for file in all_files1:
    print("filename: {0}, date: {1}".format(file.get_filename(), file.get_date_taken()))

"""
for root, dirs, files in os.walk(STR_DIR4):
    for file in files:
        move(root + os.sep + file, STR_DIR3 + os.sep + file)
        count += 1
"""
