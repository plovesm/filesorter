# @author Paul Ottley
# @copyright 2017

import os

from app import NavUtil, ImageUtils, ReportUtil

STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Pictures/images"
STR_DIR2 = r"/Volumes/Elements2TB/Backups/Pictures/images"
LOG_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/dedup_list2.txt"
DUP_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/dup_list2.txt"

all_files1 = NavUtil.walk_dir(STR_DIR1, STR_DIR1)
all_files2 = NavUtil.walk_dir(STR_DIR2, STR_DIR2)

dedupped_list = NavUtil.merge_files(all_files1, all_files2)

log = open(LOG_FILE, "w")
for file in dedupped_list[0]:
    line = file.get_filename()

    log.seek(0, 2)
    l = log.write(line)

log.close()

dup_log = open(DUP_FILE, "w")
for f in dedupped_list[1]:
    line = f.get_filename()

    dup_log.seek(0, 2)
    l = dup_log.write(line)

dup_log.close()
