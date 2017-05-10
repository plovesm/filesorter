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
# STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/Cleanup_Botched"
STR_DIR1 = r"/Users/paulottley/Desktop/Botched"

Culprits = ["/Volumes/MyBook2TB/Backups/Library/08-August_P7190292.MOV",
            "/Volumes/MyBook2TB/Backups/Library/08-August_P7200293.MOV",
            "/Volumes/MyBook2TB/Backups/Library/08-August_P7200298.MOV",
            "/Volumes/MyBook2TB/Backups/Library/08-August_P7200299.MOV",
            "/Volumes/MyBook2TB/Backups/Library/08-August_P7200315.MOV",
            "/Volumes/MyBook2TB/Backups/Library/08-August_P7200323.MOV",
            "/Volumes/MyBook2TB/Backups/Library/08-August_P7200326.MOV",
            "/Volumes/MyBook2TB/Backups/Library/08-August_P7200338.MOV",
            "/Volumes/MyBook2TB/Backups/Library/08-August_P7200339.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC240012.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC250009.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC250012.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC260025.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC260026.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC260027.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC260030.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC260031.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC270006.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC270007.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC280014_1.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC280015_1.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC280018_1.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC280020_1.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC280022_1.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC290011_1.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC290014_1.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC290018_1.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC290034.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Christmas_Time_2006-12-15_PC290035.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Evelyn Birth_2008-04-18_100_1420.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Evelyn Birth_2008-04-18_100_1421.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Evelyn Birth_2008-04-18_100_1442.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Evelyn Birth_2008-04-18_100_1443.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Evelyn Birth_2008-04-18_100_1445.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Evelyn Birth_2008-04-18_100_1465.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Evelyn Birth_2008-04-18_100_1466.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Evelyn Birth_2008-04-18_100_1493.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Evelyn Birth_2008-04-18_100_1494.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Evelyn Birth_2008-04-18_100_1495.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Evelyn Birth_2008-04-18_100_1496.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_0756.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_0757.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_0758.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_0759.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_0760.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_0761.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_0762.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_0763.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_0764.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_0765.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_0766.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_0916.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_0928.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_0959.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_1057.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_100_1058.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_A-boo-boo_to_Evelyn.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_Evelyn_Changing_table_gurgle.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_Evelyn_Changing_table_upset.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_Girlies_bathtime_play.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_Girlies_Chase_and_laugh_lots.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Family_~2009-03-01_Girlies_Crawl_and_Chase.MOV",
            "/Volumes/MyBook2TB/Backups/Library/Megan and Emily Visit_P5020066_1.MOV"]

all_files1 = NavUtil.walk_dir(STR_DIR1, STR_DIR1)

# Check date of original file

# Parse date

# Find mp4 file of same name

# Update date
count = 0
zero_count = 0
missing_filename_dt = 0
for file in all_files1:
    count += 1
    tgt_dir = file.get_tgt_dir()
    filename = file.get_filename()
    orig_date = file.get_date_taken()

    ImageUtils.get_dt_from_atom_parser(file.get_full_path())
    if "0000:00:00 00:00:00" == orig_date or "2000:01:01 00:00:00" == orig_date:
        zero_count += 1
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        # FileUtils.move_file(file.get_full_path(), tgt_dir + "Cleanup/", file.get_tgt_filename())

    m = re.search(r"(19|20)\d\d[- /.:_]?(1[012]|0?[1-9])[- /.:_]?([12][0-9]|3[01]|0?[1-9])", filename)

    # Pull full date from name
    if m is None:
        missing_filename_dt += 1
        print("***********************")

    """
    else:
        # Set the date from the filename and move it out of cleanup
        file_type = FileUtils.get_file_type(file.get_filename())
        date = ImageUtils.get_original_date(file.get_full_path())
        dt = ImageUtils.get_dt_captured_split(date)
        ImageUtils.set_date(file.get_full_path(), dt.year, dt.month, dt.day)
        # Move it out of Cleanup
        if "Cleanup/" in tgt_dir:
            tgt_dir = tgt_dir.replace("Cleanup/", "")

        FileUtils.move_file(file.get_full_path(), tgt_dir, file.get_tgt_filename())
    """
    print("Filename: {0} date: {1}".format(file.get_filename(), orig_date))

print("Total count: {0} Zero Count: {1} Missing date in filename: {2}".format(count, zero_count, missing_filename_dt))
