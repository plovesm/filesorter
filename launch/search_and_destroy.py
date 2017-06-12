# @author Paul Ottley
# @copyright 2017
import os
import re

from app import FileUtils
from app import ImageUtils

START_DIR = r"/Volumes/Elements2TB/Backups/Pictures/images"
INPUT_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/Search_and_Destroy_zeros.txt"
LOG_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/Search_and_Destroy_log.txt"

months = {"Jan": "01",
          "Feb": "02",
          "Mar": "03",
          "Apr": "04",
          "May": "05",
          "Jun": "06",
          "Jul": "07",
          "Aug": "08",
          "Sep": "09",
          "Oct": "10",
          "Nov": "11",
          "Dec": "12"}

batch_input = open(INPUT_FILE, "r")

for line in batch_input:
    line = line.rstrip()
    path, fn = os.path.split(line)

    m_date = re.search(r"\w\w\w_\d{1,2}_\d{4}", fn)

    word_date = ""
    if m_date is not None:
        word_date = m_date.group()

        word_month = word_date[:3]
        month_num = months[word_month]

        m_year = re.search(r"_\d{4}", word_date)

        word_year = ""
        if m_year is not None:
            word_year = m_year.group().replace("_", "")

        m_day = re.search(r"_\d{1,2}_", word_date)

        word_day = ""
        if m_day is not None:
            word_day = m_day.group().replace("_", "")
            if int(word_day) < 10:
                word_day = "0" + word_day

        new_fn = fn.replace("0000-00-00_" + word_date, "{0}-{1}-{2}_".format(word_year, month_num, word_day))
        new_fn = new_fn.replace("__", "_")
        print("File: {0} New: {1}".format(fn, new_fn))
        if FileUtils.does_file_exist(new_fn, path):
            print("Files exists! {0}".format(new_fn))
        else:
            os.rename(line, path + os.sep + new_fn)
"""
for root, dirs, files in os.walk(START_DIR):
    for file in files:
        new_file = file.replace(",", "")
        if file != new_file:
            print("File: {0} New File: {1}".format(file, new_file))
            os.rename(root + os.sep + file, root + os.sep + new_file)
"""
batch_input.close()
