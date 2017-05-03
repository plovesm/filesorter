"""
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
"""
import os

from app import ImageUtils

# STR_DIR1 = r"/Users/paulottley/Desktop/SortSource"
STR_DIR1 = r"/Volumes/MyBook2TB/Backups/Library/videos/Cleanup"

for root, dirs, files in os.walk(STR_DIR1):
    for file in files:
        if "20wkUltrasound" in file:
            file_name = root + os.sep + file
            ImageUtils.set_date(file_name,  # Filename
                                2006,  # Year
                                3,  # Month
                                16)  # Day

            print("New Date: {0}".format(ImageUtils.get_original_date(file_name)))


"""
file_name = r"/Volumes/MyBook2TB/Backups/Library/videos/1904/1/RingVideo_2304932614.mp4"

ImageUtils.set_date(file_name,  # Filename
                    2017,  # Year
                    3,  # Month
                    4)  # Day

print("New Date: {0}".format(ImageUtils.get_original_date(file_name)))
"""