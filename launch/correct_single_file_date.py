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
SINGLE_FILE = r"/Volumes/Elements2TB/Backups/Library/Fun_and_Games_2004_1212Image0001.mp4"

print("Old Date: {0}".format(ImageUtils.get_original_date(SINGLE_FILE)))

ImageUtils.set_date(SINGLE_FILE,  # Filename
                    "2004-12-12 00:00:00",
                    1999,  # Year
                    12,  # Month
                    1,
                    True)  # Day

print("New Date: {0}".format(ImageUtils.get_original_date(SINGLE_FILE)))
