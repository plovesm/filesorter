# @author Paul Ottley
# @copyright 2017
import os

from app import FileUtils
from app import ImageUtils

INPUT_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/Check_Dates_Missing_Embed.txt"
LOG_FILE = r"/Users/paulottley/PycharmProjects/filesorter/test/Check_Dates_log.txt"

input = open(INPUT_FILE, "r")

for line in input:
    line = line.rstrip()
    path, fn = os.path.split(line)
    dt = ImageUtils.get_dt_from_name(line)
    print(dt)
    # ImageUtils.set_date(line, dt)
    FileUtils.move_file(line, path + "/Embed_fail/", fn)
    print(ImageUtils.get_dt_from_atom_parser(line))
    # print(line)

input.close()
