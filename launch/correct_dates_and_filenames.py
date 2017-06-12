# @author Paul Ottley
# @copyright 2017
import time
import datetime
import os
import re

from app import FileUtils
from app import ImageUtils

count = 0
zero_count = 0

# STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library"
STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Videos/Unsupported_Converted"
# STR_DIR1 = r"/Users/paulottley/Desktop/Botched"

problem_files = []

start_time = datetime.datetime.now()
print("Correct Date started at {0}:".format(start_time))

for root, dirs, files in os.walk(STR_DIR1):
    for file in files:
        """
        if "dog" is "dog":
            if "cat" is "cat":
                root = r"/Volumes/Elements2TB/Backups/Library"
                file = "Fun_and_Games_2004_1212Image0001.mp4"
        """
        full_filename = root + os.sep + file

        if "." is file[0]:
            print("Moving..." + full_filename)
            FileUtils.move_file(full_filename, r"/Volumes/Elements2TB/Backups/Trash/", file)

        else:
            orig_datetime = ImageUtils.get_original_date(full_filename)
            orig_date = orig_datetime.split(" ")[0]
            new_file = file

            if "0000" in orig_date:
                if file[0] is not ".":
                    zero_count += 1

                    # print("~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("0000000 Filename: {0} date: {1}".format(file, orig_date))

            # First, set the date so it is consistent
            # ImageUtils.set_date(full_filename, orig_datetime)

            # Next, Clean up the name,
            #  - remove all spaces
            #  - check if there is a date mismatch with filename and take earliest
            #  - remove oddly formatted dates in the filename
            #  - Rename file to have consistent date pattern on the beginning

            new_file = new_file.replace("images_", "")
            new_file = new_file.replace(" ", "_")

            print("File: {0} Date: {1}".format(file, orig_datetime))

            date_frm_filename = ImageUtils.get_dt_from_name(file)
            problem_files_str = ""

            if date_frm_filename is not None:
                if date_frm_filename[:4] == orig_date[:4]:
                    new_file = re.sub(r"(19|20)\d\d[- /.:_]?(1[012]|0?[1-9])[- /.:_]?([12][0-9]|3[01]|0?[1-9])[- /:_]?",
                                      "",
                                      new_file)
                    problem_files_str = "Matched "
                else:
                    problem_files_str = "No Match "

            # Format for consistancy
            orig_date = re.sub(r"\D", "-", orig_date)

            if problem_files_str is not "":
                problem_files.append(problem_files_str +
                                     "Date 1: {0} and Date 2: {1} Filename: {2} New_File: {3}".format(
                                                                                            date_frm_filename[:4],
                                                                                            orig_date[:4],
                                                                                            file,
                                                                                            orig_date + "_" + new_file))

            # if orig_date[len(orig_date) - 1] is "_":
            new_file = orig_date + "_" + new_file

            while "__" in new_file:
                new_file = new_file.replace("__", "_")

            while FileUtils.does_file_exist(new_file, root + os.sep) is True:
                print("Dup: " + new_file)
                new_file = FileUtils.add_suffix(new_file, "1")

            full_new_file = root + os.sep + new_file

            os.rename(full_filename, full_new_file)
            print(full_new_file)

        count += 1

print("Total count: {0} Zero Count: {1}".format(count, zero_count))

end_time = datetime.datetime.now()
print("Correct Date ended at {0}:".format(end_time))

print("Start time: {0} End time: {1}".format(start_time, end_time))

for f in problem_files:
    print(f)
