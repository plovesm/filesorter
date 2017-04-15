# @author Paul Ottley
# @copyright 2017

from app import Mov
from app import FileSorter
import datetime
import subprocess

import os

STR_DIR1 = r"/Users/paulottley/Movies/iMovie Library.imovielibrary/4-2-17/Original Media"
STR_DIR2 = r"/Volumes/OttFamilyShare/Backups/Pictures"
STR_DIR3 = r"/Volumes/MyBook2TB/Backups/Library/wmv"
STR_DIR4 = r"/Users/paulottley/Desktop/SortSource"
STR_DIR5 = r"/Users/paulottley/Google Drive/MomsDadsPhotos"

TGT_DIR1 = r"/Users/paulottley/Desktop/SortTarget"

fs = FileSorter(STR_DIR4, TGT_DIR1)

all_files1 = fs.walk_dir(STR_DIR4, TGT_DIR1)
print("Before")
for file in all_files1:
    print("filename: {0}, date: {1}".format(file.get_filename(), file.get_date_taken()))

"""
testfile = Mov(all_files1[0].get_full_path())
testfile2 = Mov(all_files1[1].get_full_path())

datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

dt = datetime.date(2013, 5, 17)

testfile2.set_date(dt)

testfile.parse()
testfile2.parse()
"""
"""
for line in parsed1:
    if "Creation time:" in line:
        print(line)
"""
dt = datetime.date(2013, 5, 17)
strdt = dt.strftime("%Y-%m-%d %H:%M:%S")

m = Mov(all_files1[1].get_full_path())
m.parse()

if strdt is not "":
    d = datetime.datetime.strptime(strdt, "%Y-%m-%d %H:%M:%S")
    m.set_date(d)


subprocess.call(["python", "../app/modmy.py", all_files1[1].get_full_path(), strdt])
print("After")
for file in all_files1:
    print("filename: {0}, date: {1}".format(file.get_filename(), file.get_date_taken()))
