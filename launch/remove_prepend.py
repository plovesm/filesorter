# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch
import os
import re
from shutil import move

from app import NavUtil, FileUtils, ImageUtils

STR_DIR1 = r"/Users/paulottley/Movies/iMovie Library.imovielibrary/4-2-17/Original Media"
STR_DIR2 = r"/Volumes/OttFamilyShare/Backups/Library/To be imported"
STR_DIR3 = r"/Volumes/MyBook2TB/Backups/Library"
# STR_DIR3 = r"/Volumes/MyBook2TB/Backups/SortTarget"
TGT_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/videos"

for root, dirs, files in os.walk(STR_DIR3):
    for file in files:
        if "...." in file:
            new_file = file.replace("...", "")
            print(root + os.sep + new_file)
            os.rename(root + os.sep + file, root + os.sep + new_file)
        if "((d))" in file:
            new_file = file.replace("((d))", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")

        new_file = ImageUtils.remove_false_datestamp(file)
        if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
            print(root + os.sep + new_file)
            os.rename(root + os.sep + file, root + os.sep + new_file)
        else:
            print(new_file + "file exists")

"""
        if "20170103-023237_" in file:
            new_file = file.replace("20170103-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20170102-033745_" in file:
            new_file = file.replace("20170102-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20150803-042006_" in file:
            new_file = file.replace("20150803-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20150803-225908_" in file:
            new_file = file.replace("20150803-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20150803-230404_" in file:
            new_file = file.replace("20150803-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20150803-230917_" in file:
            new_file = file.replace("20150803-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20150807-003916_" in file:
            new_file = file.replace("20150807-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20150906-000050_" in file:
            new_file = file.replace("20150906-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20150906-010536_" in file:
            new_file = file.replace("20150906-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20150906-011751_" in file:
            new_file = file.replace("20150906-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20150911-210756_" in file:
            new_file = file.replace("20150911-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20150914-202617_" in file:
            new_file = file.replace("20150914-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151003-" in file:
            new_file = file.replace("20151003-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151021-123634_" in file:
            new_file = file.replace("20151021-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151103-144306_" in file:
            new_file = file.replace("20151103-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151112-030438_" in file:
            new_file = file.replace("20151112-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151124-154217_" in file:
            new_file = file.replace("20151124-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151126-182526_" in file:
            new_file = file.replace("20151126-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151209-153700_" in file:
            new_file = file.replace("20151209-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151215-030819_" in file:
            new_file = file.replace("20151215-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151215-041215_" in file:
            new_file = file.replace("20151215-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151215-042058_" in file:
            new_file = file.replace("20151215-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151216-044049_" in file:
            new_file = file.replace("20151216-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151216-152208_" in file:
            new_file = file.replace("20151216-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151216-161005_" in file:
            new_file = file.replace("20151216-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151218-" in file:
            new_file = file.replace("20151218-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151219-" in file:
            new_file = file.replace("20151219-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151220-" in file:
            new_file = file.replace("20151220-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151221-" in file:
            new_file = file.replace("20151221-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151222-" in file:
            new_file = file.replace("20151222-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151223-" in file:
            new_file = file.replace("20151223-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151224-" in file:
            new_file = file.replace("20151224-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151225-" in file:
            new_file = file.replace("20151225-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151226-" in file:
            new_file = file.replace("20151226-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151227-" in file:
            new_file = file.replace("20151227-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151228-" in file:
            new_file = file.replace("20151228-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151229-" in file:
            new_file = file.replace("20151229-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151230-" in file:
            new_file = file.replace("20151230-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20151231-" in file:
            new_file = file.replace("20151231-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160101-" in file:
            new_file = file.replace("20160101-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160102-" in file:
            new_file = file.replace("20160102-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160105-" in file:
            new_file = file.replace("20160105-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160106-" in file:
            new_file = file.replace("20160106-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160109-" in file:
            new_file = file.replace("20160109-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160110-" in file:
            new_file = file.replace("20160110-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160112-" in file:
            new_file = file.replace("20160112-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160114-" in file:
            new_file = file.replace("20160114-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160116-" in file:
            new_file = file.replace("20160116-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160123-" in file:
            new_file = file.replace("20160123-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160130-" in file:
            new_file = file.replace("20160130-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160131-" in file:
            new_file = file.replace("20160131-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160204-" in file:
            new_file = file.replace("20160204-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160208-" in file:
            new_file = file.replace("20160208-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160214-" in file:
            new_file = file.replace("20160214-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160216-" in file:
            new_file = file.replace("20160216-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160217-" in file:
            new_file = file.replace("20160217-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20160217-" in file:
            new_file = file.replace("20160217-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")
        if "20141207-" in file:
            new_file = file.replace("20141207-", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")


fs = FileSorter(STR_DIR2, STR_DIR2)

all_files1 = fs.walk_dir(STR_DIR2, STR_DIR2)

file_lists = [all_files1, []]  # fs.mark_duplicates(all_files1)

for x in file_lists[0]:
    filename_arr = x.get_tgt_filename().rpartition("To be imported_")
    x.set_tgt_filename(filename_arr[2])

fs.move_files(file_lists[0])

fs.final_report(file_lists)
"""