# @author Paul Ottley
# @copyright 2017
import time
import datetime
import os
import re

from app import FileUtils
from app import ImageUtils
from app import Rules

count = 0
zero_count = 0

STR_DIR1 = r"/Users/paulottley/Desktop/SortSource"
# STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Pictures/images"

files_batch = r"/Users/paulottley/PycharmProjects/filesorter/test/Filename_Changes.txt"

problem_files = []

# Open file log with write privileges
files_log = open(files_batch, "w")

start_time = datetime.datetime.now()
print("Correct Date started at {0}:".format(start_time))

for root, dirs, files in os.walk(STR_DIR1):
    for file in files:

        full_filename = root + os.sep + file

        if "." is file[0]:
            print("Moving..." + full_filename)
            FileUtils.move_file(full_filename, r"/Volumes/MyBook2TB/Backups/Trash/", file)

        else:
            date_taken = ImageUtils.get_dt_from_name(file)
            orig_datetime = ImageUtils.get_original_date(full_filename)
            orig_date = orig_datetime.split(" ")[0]
            new_file = file

            # TODO Figure out if there is a need to reconcile date_taken and orig_date

            if "0000" in orig_date:
                if file[0] is not ".":
                    zero_count += 1
                    print("0000000 Filename: {0} date: {1}".format(file, orig_date))

            # First, set the date so it is consistent
            # ImageUtils.set_date(full_filename, orig_datetime)

            # Next, Clean up the name,
            #  - remove all spaces
            #  - check if there is a date mismatch with filename and take earliest
            #  - remove oddly formatted dates in the filename
            #  - Rename file to have consistent date pattern on the beginning

            # print("File: {0} Date: {1}".format(file, orig_datetime))

            problem_files_str = ""

            if date_taken is not None:
                # Format for consistancy
                orig_date_chk = re.sub(r"\D", "", orig_date)
                date_frm_filename_chk = re.sub(r"\D", "", date_taken)

                if date_frm_filename_chk[:6] == orig_date_chk[:6]:

                    problem_files_str = "Matched "
                else:
                    if int(date_frm_filename_chk) < int(orig_date_chk) or "0000" in orig_date:
                        orig_date = date_taken

                    problem_files_str = "No Match "

            # Format for consistancy
            orig_date = re.sub(r"\D", "-", orig_date)

            # Remove dates from filename
            new_file = re.sub(Rules.get_date_regex_word(), "", new_file)
            new_file = re.sub(Rules.get_date_regex_prefix(), "", new_file)

            new_file = new_file.replace("~", "")
            new_file = new_file.replace("copy", "")
            new_file = new_file.replace("images_", "")
            new_file = new_file.replace("Pictures to sort and save", "IMG")
            new_file = new_file.replace("_.", ".")
            new_file = new_file.replace(" ", "_")

            new_file = orig_date + "_" + new_file

            while "__" in new_file:
                new_file = new_file.replace("__", "_")

            if problem_files_str is not "":
                problem_files.append(problem_files_str +
                                     "Date 1: {0} and Date 2: {1} Filename: {2} New_File: {3}".format(
                                         date_taken[:4],
                                         orig_date[:4],
                                         file,
                                         new_file))

            while FileUtils.does_file_exist(new_file, root + os.sep) is True:
                print("Dup: " + new_file)
                new_file = FileUtils.add_suffix(new_file, "1")

            full_new_file = root + os.sep + new_file

            # os.rename(full_filename, full_new_file)
            files_log.write("Old: " + full_filename + "\n")
            files_log.write("New: " + full_new_file + "\n")

        count += 1

print("Total count: {0} Zero Count: {1}".format(count, zero_count))

end_time = datetime.datetime.now()
print("Correct Date ended at {0}:".format(end_time))

print("Start time: {0} End time: {1}".format(start_time, end_time))

for f in problem_files:
    print(f)

# clean up
files_log.close()
