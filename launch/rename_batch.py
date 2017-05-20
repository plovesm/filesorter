# @author Paul Ottley
# @copyright 2017
import os

from app import FileUtils
from app import ImageUtils

ORIG_INPUT_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/Check_Dates_Zero.txt"
NEW_INPUT_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/Check_Dates_Zero_Rename.txt"
LOG_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/Check_Dates_log.txt"

orig_input = open(ORIG_INPUT_FILE, "r")
orig_arr = orig_input.readlines()
orig_input.close()

new_input = open(NEW_INPUT_FILE, "r")
new_arr = new_input.readlines()
new_input.close()

print("Orig_input length: {0} New_Input length {1}: ".format(len(orig_arr), len(new_arr)))

if len(orig_arr) == len(new_arr):
    currentIndex = 0
    for name in orig_arr:
        orig_name = name.rstrip()
        new_name = new_arr[currentIndex].rstrip()

        orig_path, orig_fn = os.path.split(orig_name)
        new_path, new_fn = os.path.split(new_name)

        os.rename(orig_name, new_name)

        currentIndex += 1
