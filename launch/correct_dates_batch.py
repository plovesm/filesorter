# @author Paul Ottley
# @copyright 2017
import os

from app import FileUtils
from app import ImageUtils

START_DIR1 = r"/Volumes/MyBook2TB/Backups/Videos/Unsupported_Converted"
INPUT_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/Check_Dates_Zero_Rename.txt"
LOG_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/Check_Dates_log.txt"

batch = False

if batch is True:

    batch_input = open(INPUT_FILE, "r")

    for line in batch_input:
        line = line.rstrip()
        path, fn = os.path.split(line)
        dt = ImageUtils.get_dt_from_name(fn)
        print(dt)
        ImageUtils.set_date(line, dt)
        # FileUtils.move_file(line, path + "/Zeros/", fn)
        print(ImageUtils.get_dt_from_atom_parser(line))
        print(line)

    batch_input.close()

else:
    for root, dirs, files in os.walk(START_DIR1):
        for file in files:
            full_filename = root + os.sep + file

            if "." is file[0]:
                print("Moving..." + full_filename)
                FileUtils.move_file(full_filename, r"/Volumes/MyBook2TB/Backups/Trash/", file)
            else:

                dt = ImageUtils.get_dt_from_name(file)
                print(dt)
                ImageUtils.set_date(full_filename, dt)
