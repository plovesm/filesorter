# @author Paul Ottley
# @copyright 2017

# Purpose is to extract all files from db and create flat file to batch edits

from app import DatabaseUtil
from app import Rules

files_batch = r"/Users/paulottley/PycharmProjects/filesorter/test/All_Files_Init_Log.txt"

# Open file log with write privileges
files_log = open(files_batch, "w")

# Open the database
conn, cur = DatabaseUtil.open_connection()

records = DatabaseUtil.read_all_records(cur)

for record in records:
    if Rules.get_debug() is True:
        print(record)

    directory = record[5]
    filename = record[1]
    full_path = directory + filename + "\n"

    files_log.write(full_path)

# clean up
files_log.close()
DatabaseUtil.close_connection(conn)