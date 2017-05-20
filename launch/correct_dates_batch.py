# @author Paul Ottley
# @copyright 2017
import os

from app import FileUtils
from app import ImageUtils

INPUT_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/Check_Dates_Zero_Rename.txt"
LOG_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/Check_Dates_log.txt"

batch_input = open(INPUT_FILE, "r")

for line in batch_input:
    line = line.rstrip()
    path, fn = os.path.split(line)
    dt = ImageUtils.get_dt_from_name(fn)
    print(dt)
    ImageUtils.set_date(line, dt)
    # FileUtils.move_file(line, path + "/Zeros/", fn)
    print(ImageUtils.get_dt_from_atom_parser(line))
    print(line)

batch_input.close()
