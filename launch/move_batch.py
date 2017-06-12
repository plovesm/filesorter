# @author Paul Ottley
# @copyright 2017
import os

from app import FileUtils
from app import ImageUtils

INPUT_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/unsupported_files.txt"
LOG_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/Check_Dates_log.txt"

orig_input = open(INPUT_FILE, "r")
orig_arr = orig_input.readlines()
orig_input.close()

currentIndex = 0
for name in orig_arr:
    orig_name = name.rstrip()

    orig_path, orig_fn = os.path.split(orig_name)
    print("Moving %s" % orig_name)

    FileUtils.copy_file(orig_name, "/Volumes/MyBook2TB/Backups/Library/unsupported/", orig_fn)

    currentIndex += 1

print("Total files moved: %d" % currentIndex)
