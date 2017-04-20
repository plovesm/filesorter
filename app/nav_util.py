# FileSorter
# @author Paul Ottley
# @copyright 2017

import os
import datetime
import time

from app import FileUtils
from app import ImageUtils
from app import Rules
from objects import FSfile

"""
Constants
"""
SEPARATOR = os.sep
IMG_DIR = Rules.get_img_dir()
VID_DIR = Rules.get_vid_dir()
OTH_DIR = Rules.get_oth_dir()
IMG_TAG = Rules.get_img_tag()
VID_TAG = Rules.get_vid_tag()
OTH_TAG = Rules.get_oth_tag()

IMG_TYPES = Rules.get_img_types()
VID_TYPES = Rules.get_vid_types()


class NavUtil:

    """
    @description: Walk a directory and build out a file collection and metadata
    """
    @staticmethod
    def walk_dir(dir_to_walk, tgt_dir):
        # Print time started
        ts = time.time()
        start_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print("Walk Dir started at {0}:".format(start_time))

        # Build empty container for the files
        all_files = []

        if os.path.isdir(dir_to_walk):
            # Walk the directory and count the files
            for root, dirs, files in os.walk(dir_to_walk):
                for file in files:
                    # Step 1: Build the file object with name and location
                    fs_file = FSfile()
                    fs_file.set_filename(file)
                    fs_file.set_src_dir(root + SEPARATOR)
                    fs_file.set_tgt_dir(tgt_dir + SEPARATOR)

                    # Step 2: Add metadata of size and date to object
                    fs_file.set_size(FileUtils.get_file_size(fs_file.get_full_path()))
                    fs_file.set_date_taken(ImageUtils.get_original_date(fs_file.get_full_path()))

                    # Step 3: Determine file type and tag
                    current_file = NavUtil.sort_file_type(fs_file)

                    # Step 4: Add file to collection
                    all_files.append(current_file)

        # Print time ended
        ts2 = time.time()
        end_time = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
        print("Walk Dir completed at {0} with {1} files collected.".format(end_time, len(all_files)))

        return all_files

    @staticmethod
    def sort_file_type(fs_file):
        # Initialize type as other
        file_type = OTH_TAG
        tgt_folder = OTH_DIR

        # Get the extension
        f_ext = FileUtils.get_file_type(fs_file.get_filename())

        # Check extension and switch to image or video
        if f_ext in IMG_TYPES:
            file_type = IMG_TAG
            tgt_folder = IMG_DIR
        elif f_ext in VID_TYPES:
            file_type = VID_TAG
            tgt_folder = VID_DIR

        return NavUtil.tag_file(fs_file, file_type, tgt_folder)

    @staticmethod
    def mark_duplicates(all_files):
        """

        :rtype: tuple[all_files, duplicates]
        """
        # Print start time
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

        # Print end time
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
        file_set_pair1 = NavUtil.mark_duplicates(file_set1)
        file_set_pair2 = NavUtil.mark_duplicates(file_set2)

        # Combine the two sets
        full_file_set = file_set_pair1[0] + file_set_pair2[0]

        # De-dup the full set
        full_file_set_pair = NavUtil.mark_duplicates(full_file_set)
        full_file_duplicates = full_file_set_pair[1] + file_set_pair1[1] + file_set_pair2[1]

        return full_file_set_pair[0], full_file_duplicates

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
    def tag_file(fs_file, fs_file_type, tgt_folder):
        fs_file.set_type(fs_file_type)
        fs_file.set_tgt_folder(tgt_folder + SEPARATOR)
        # return FileSorter.prepend_folder_name(fs_file)
        fs_file.set_tgt_filename(fs_file.get_filename())
        return fs_file

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
