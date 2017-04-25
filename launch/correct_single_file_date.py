"""
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
"""
from app import ImageUtils

file_name = r"/Volumes/MyBook2TB/Backups/Library/videos/1904/1/RingVideo_2304932614.mp4"

ImageUtils.set_date(file_name,  # Filename
                    2017,  # Year
                    3,  # Month
                    4)  # Day

print("New Date: {0}".format(ImageUtils.get_original_date(file_name)))
