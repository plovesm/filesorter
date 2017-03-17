# FileSorter
# @author Paul Ottley
# @copyright 2017

import os
import datetime
import time
from decimal import Decimal

from app import EmailUtils
from app import FileUtils
from app import ImageUtils
from objects import FSfile

SEPARATOR = "/"
IMG_DIR = "images"
VID_DIR = "videos"
OTH_DIR = "other"
IMG_TAG = "i"
VID_TAG = "v"
OTH_TAG = "o"

IMG_TYPES = ["jpg", "png", "gif", "bmp", "jpeg", "nef", "tif"]
VID_TYPES = ["mpg", "mp4", "mpeg", "flv", "wmv", "mov", "avi", "3gp", "dv", "m4v"]


class FileSorter:

    def __init__(self, start_dir, target_dir):
        print("Initializing FileSorter...")
        self.start_dir = start_dir
        self.target_dir = target_dir

    def default_start(self):
        start_dir = self.start_dir
        tgt_dir = self.target_dir

        all_files = FileSorter.walk_dir(start_dir, tgt_dir)

        file_lists = FileSorter.mark_duplicates(all_files)

        FileSorter.move_files(file_lists[0])
        # FileSorter.copy_files(file_lists[0])

        FileSorter.final_report(file_lists)

    @staticmethod
    def walk_dir(dir_to_walk, tgt_dir):
        ts = time.time()
        start_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print("Walk Dir started at {0}:".format(start_time))

        all_files = []

        if os.path.isdir(dir_to_walk):
            # Walk the directory and count the files
            for root, dirs, files in os.walk(dir_to_walk):
                for file in files:
                    # Check the type of file
                    fs_file = FSfile()
                    fs_file.set_filename(file)
                    fs_file.set_src_dir(root + SEPARATOR)
                    fs_file.set_tgt_dir(tgt_dir + SEPARATOR)
                    fs_file.set_size(FileUtils.get_file_size(fs_file.get_full_path()))
                    fs_file.set_date_taken(ImageUtils.get_dt_captured(fs_file.get_full_path()))
                    current_file = FileSorter.sort_file_type(fs_file)

                    # if current_file.get_type() == "o":
                    all_files.append(current_file)
            ts2 = time.time()
            end_time = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
            print("Walk Dir completed at {0} with {1} files collected. {2} GB".format(end_time,
                                                                                      FileSorter.get_type_count(
                                                                                          all_files),
                                                                                      FileSorter.calc_total_files_size(
                                                                                          all_files)))

        return all_files

    @staticmethod
    def sort_file_type(fs_file):
        file_type = OTH_TAG
        tgt_folder = OTH_DIR

        # Get the extension
        f_ext = FileUtils.get_file_type(fs_file.get_filename())

        # Count by type and fill array
        if f_ext in IMG_TYPES:
            file_type = IMG_TAG
            tgt_folder = IMG_DIR
        elif f_ext in VID_TYPES:
            file_type = VID_TAG
            tgt_folder = VID_DIR

        if fs_file.get_date_taken() is not "" and fs_file.get_date_taken() is not None:
            print("Date Taken: " + str(fs_file.get_date_taken()))
            dt_split = ImageUtils.get_dt_captured_split(fs_file.get_full_path())
            tgt_folder = "{0}{1}{2}{3}{4}".format(tgt_folder, SEPARATOR, dt_split[0], SEPARATOR, dt_split[1])

        return FileSorter.tag_file(fs_file, file_type, tgt_folder)

    @staticmethod
    def mark_duplicates(all_files):
        """

        :rtype: tuple[all_files, duplicates]
        """
        ts = time.time()
        start_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print("Mark Duplicates: " + start_time)

        duplicates = []
        dedupped_file_set = []

        # Make a copy to test
        all_files_test = all_files.copy()

        for x in all_files:
            for y in all_files_test:
                if x != y and x.get_size() == y.get_size():
                    if FileUtils.is_file_dup(x.get_full_path(), y.get_full_path()):
                        duplicates.append(y)
                        all_files.remove(y)
                        all_files_test.remove(y)

        dedupped_file_set += all_files

        ts2 = time.time()
        end_time = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
        print("Mark Duplicates completed at {0} with {1} files collected".format(end_time, len(dedupped_file_set)))

        return dedupped_file_set, duplicates

    @staticmethod
    def merge_files(file_set1, file_set2):
        """

        :rtype: tuple[all_files, duplicates]
        """
        # De-dup each set independently
        file_set_pair1 = FileSorter.mark_duplicates(file_set1)
        file_set_pair2 = FileSorter.mark_duplicates(file_set2)

        # Combine the two sets
        full_file_set = file_set_pair1[0] + file_set_pair2[0]

        # De-dup the full set
        full_file_set_pair = FileSorter.mark_duplicates(full_file_set)
        full_file_duplicates = full_file_set_pair[1] + file_set_pair1[1] + file_set_pair2[1]

        return full_file_set_pair[0], full_file_duplicates

    @staticmethod
    def final_report(file_lists):
        all_files = file_lists[0]
        duplicates = file_lists[1]
        total_count = FileSorter.get_type_count(all_files)
        total_size = FileSorter.calc_total_files_size(all_files)
        image_count = FileSorter.get_type_count(all_files, IMG_TAG)
        image_perc = FileSorter.get_formatted_percentage(image_count, total_count)
        image_size = FileSorter.calc_total_files_size(all_files, IMG_TAG)
        vid_count = FileSorter.get_type_count(all_files, VID_TAG)
        vid_perc = FileSorter.get_formatted_percentage(vid_count, total_count)
        vid_size = FileSorter.calc_total_files_size(all_files, VID_TAG)
        other_count = FileSorter.get_type_count(all_files, OTH_TAG)
        other_perc = FileSorter.get_formatted_percentage(other_count, total_count)
        other_size = FileSorter.calc_total_files_size(all_files, OTH_TAG)

        msg = "Total files= {0} Total Size= {1} GB".format(total_count, total_size)
        msg += "\nTotal duplicate files= {0}".format(FileSorter.get_type_count(duplicates))
        msg += "\nImage count= {0} ({1}%) size= {2} GB".format(image_count, image_perc, image_size)
        msg += "\nVideo count= {0} ({1}%) size= {2} GB".format(vid_count, vid_perc, vid_size)
        msg += "\nOther count= {0} ({1}%) size= {2} GB".format(other_count, other_perc, other_size)
        msg += "\nFile Name= {0}, Size= {1}, Type= {2}".format(all_files[0].get_filename(),
                                                            all_files[0].get_size(),
                                                            all_files[0].get_type())

        msg += "\nSize of all duplicates= {0} GB".format(FileSorter.calc_total_files_size(duplicates))
        EmailUtils.send_email(msg)
        print(msg)

    @staticmethod
    def move_files(all_files):
        print("Total files to move {0}".format(len(all_files)))

        for x in all_files:
            FileUtils.move_file(x.get_full_path(),
                                "{0}{1}".format(x.get_tgt_dir(), x.get_tgt_folder()), x.get_tgt_filename())

    @staticmethod
    def copy_files(all_files):
        print("Total files to copy {0}".format(len(all_files)))

        for x in all_files:
            FileUtils.copy_file(x.get_full_path(),
                                "{0}{1}".format(x.get_tgt_dir(), x.get_tgt_folder()), x.get_tgt_filename())

    @staticmethod
    def format_four_places(num):
        four_places = Decimal(10) ** -4

        return Decimal(num).quantize(four_places)

    @staticmethod
    def calc_total_files_size(files_arr, f_type=None):
        total_size = 0
        try:
            for x in files_arr:
                if f_type is None or x.get_type() is f_type:
                    total_size += x.get_size()

            return FileSorter.format_four_places(total_size / 1000000000)
        except TypeError:
            return -1

    @staticmethod
    def get_type_count(all_files, f_type=None):
        count = 0

        if f_type is None:
            try:
                return len(all_files)
            except TypeError:
                return -1
        else:
            for x in all_files:
                if x.get_type() == f_type:
                    count += 1

        return count

    @staticmethod
    def tag_file(fs_file, fs_file_type, tgt_folder):
        fs_file.set_type(fs_file_type)
        fs_file.set_tgt_folder(tgt_folder + SEPARATOR)
        return FileSorter.prepend_folder_name(fs_file)

    @staticmethod
    def get_formatted_percentage(numerator, denominator):
        return FileSorter.format_four_places((numerator / denominator) * 100)

    @staticmethod
    def prepend_folder_name(file):
        src_dir = file.get_src_dir()
        src_path = []
        if None is not src_dir and src_dir.endswith(SEPARATOR):
            src_path = src_dir.rsplit(SEPARATOR, maxsplit=2)

        try:
            file.set_tgt_filename("{0}_{1}".format(src_path[1], file.get_filename()))
        except IndexError:
            print("No source directory found")

        return file
