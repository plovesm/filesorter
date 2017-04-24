# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch
import os

from app import NavUtil, ImageUtils, ReportUtil

STR_DIR1 = r"/Users/paulottley/Movies/iMovie Library.imovielibrary/4-2-17/Original Media"
STR_DIR2 = r"/Volumes/OttFamilyShare/Backups/Pictures"
STR_DIR3 = r"/Volumes/MyBook2TB/Backups/Library"
STR_DIR4 = r"/Users/paulottley/Google Drive/MomsDadsPhotos"

TGT_DIR1 = r"/Volumes/MyBook2TB/Backups/SortTarget"

all_files1 = NavUtil.walk_dir(STR_DIR3, STR_DIR3)

file_lists = [all_files1, []]

for file in all_files1:
    # noinspection PyBroadException
    try:
        dt = ImageUtils.get_dt_captured_split(file.get_date_taken())
        file.set_tgt_dir("{0}{1}{2}{3}{4}{5}".format(file.get_tgt_dir(),
                                                     file.get_tgt_folder(),
                                                     dt.year,
                                                     os.sep,
                                                     dt.month,
                                                     os.sep))
        # print(file.get_full_tgt_path())
    except Exception as err:
        print("Date failed on: {0}".format(file.get_filename()))
        file.set_tgt_dir(file.get_tgt_dir() + os.sep + "date_err")

NavUtil.move_files(all_files1)

ReportUtil.final_report(file_lists)
