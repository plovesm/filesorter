# @author Paul Ottley
# @copyright 2017
# File used to start the FilesSorter launch
import os
import re

from app import FileUtils
from app import ImageUtils
from app import NavUtil

# STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/m4v"
# STR_DIR1 = r"/Users/paulottley/Desktop/SortSource"
# STR_DIR1 = r"/Volumes/Macintosh HD/Users/paulottley/Movies/iMovie Library.imovielibrary/5-1-17/Original Media"
# STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/videos/Cleanup"
STR_DIR1 = r"/Volumes/Elements2TB/Backups/Library"
# STR_DIR1 = r"/Users/paulottley/Desktop/Botched"
LOG_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/Check_Dates_log_after.txt"

all_files1 = NavUtil.walk_dir(STR_DIR1, STR_DIR1)

# Check date of original file

# Parse date

# Find mp4 file of same name

# Update date
count = 0
zero_count = 0
missing_filename_dt = 0
missing_embed_dt = 0
mismatched_dt = 0
log = open(LOG_FILE, "w")

for file in all_files1:
    count += 1
    tgt_dir = file.get_tgt_dir()
    filename = file.get_filename()
    orig_date = file.get_date_taken()
    full_path = file.get_full_path()

    line = ""

    dt_frm_embed = ImageUtils.get_dt_from_atom_parser(full_path)
    dt_frm_filename = ImageUtils.get_dt_from_name(filename)

    if "0000:00:00 00:00:00" == orig_date or "2000:01:01 00:00:00" == orig_date:
        zero_count += 1
        line += "\nZero Date in Filename: {0}".format(full_path)

    if None is dt_frm_filename:
        missing_filename_dt += 1
        line += "\nMissing Date in Filename: {0}".format(full_path)
    elif None is dt_frm_embed:
        missing_embed_dt += 1
        line += "\nMissing Date in Embed: {0}".format(full_path)
    else:
        if dt_frm_filename[:4] != dt_frm_embed[:4]:
            mismatched_dt += 1
            line += "\nDates don't match: {0} {1} {2}".format(dt_frm_embed, dt_frm_filename, full_path)

    line += "\nFilename: {0} date: {1}".format(filename, orig_date)
    log.seek(0,2)
    l = log.write(line)

log.seek(0, 2)
l = log.write("\nTotal count: {0} Zero Count: {1} Missing date in filename: {2} Missing Embed: {3} Mismatch: {4}".format(
    count,
    zero_count,
    missing_filename_dt,
    missing_embed_dt,
    mismatched_dt))

log.close()
