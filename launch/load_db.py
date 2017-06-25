# @author Paul Ottley
# @copyright 2017
import os

from app import DatabaseUtil
from app import NavUtil
from app import Rules

TEST_SRC_DIR = r"/Users/paulottley/Desktop/SortSource"
TEST_TGT_DIR = r"/Users/paulottley/Desktop/SortSource"

SRC_DIR = r"/Volumes/MyBook2TB/Backups/Pictures/images"
TGT_DIR = r"/Volumes/MyBook2TB/Backups/Pictures/images"

all_files = NavUtil.walk_dir(SRC_DIR, TGT_DIR)

files, duplicates = NavUtil.mark_duplicates(all_files)

print("Number of files: {0} Number of Dups {1}".format(len(files), len(duplicates)))

conn, cur = DatabaseUtil.open_connection()

DatabaseUtil.create_files_table(cur)

for file in files:
    # Store metadata in db
    DatabaseUtil.insert_record(cur, file)

records = DatabaseUtil.read_all_records(cur)

if Rules.get_debug() is True:
    for record in records:
        print(record)

for file in duplicates:
    file.set_tgt_dir(file.get_tgt_dir() + "dups" + os.sep)

NavUtil.move_files(duplicates)

DatabaseUtil.close_connection(conn)
