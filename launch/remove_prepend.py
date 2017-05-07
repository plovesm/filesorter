# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch
import os
import re
from shutil import move

from app import NavUtil, FileUtils, ImageUtils

STR_DIR1 = r"/Users/paulottley/Movies/iMovie Library.imovielibrary/4-2-17/Original Media"
STR_DIR2 = r"/Volumes/OttFamilyShare/Backups/Library/To be imported"
STR_DIR3 = r"/Volumes/MyBook2TB/Backups/Library/videos/Cleanup"
# STR_DIR3 = r"/Volumes/MyBook2TB/Backups/SortTarget"
TGT_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/videos/Cleanup"

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

        m = re.search(r"20\d{2}-\d{2}-\d{1}\D", file)

        # Pull full date from name
        if m is not None:
            print(file + " file exists")
        if " " in file:
            new_file = file.replace(" ", "")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")

        if "Birth" in file:
            new_file = file.replace("Birth", "_Birth")
            if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
                print(root + os.sep + new_file)
                os.rename(root + os.sep + file, root + os.sep + new_file)
            else:
                print(new_file + "file exists")

        """
        new_file = ImageUtils.remove_false_datestamp(file)
        if FileUtils.does_file_exist(new_file, root + os.sep) is not True:
            print(root + os.sep + new_file)
            os.rename(root + os.sep + file, root + os.sep + new_file)
        else:
            print(new_file + "file exists")
        """