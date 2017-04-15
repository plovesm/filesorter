# FileSorter
# @author Paul Ottley
# @copyright 2017
import os

from app import EmailUtils
from app import NavUtil
from app import Rules

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


class ReportUtil:

    @staticmethod
    def final_report(file_lists):
        all_files = file_lists[0]
        duplicates = file_lists[1]
        total_count = NavUtil.get_type_count(all_files)
        total_size = NavUtil.calc_total_files_size(all_files)
        image_count = NavUtil.get_type_count(all_files, IMG_TAG)
        image_perc = NavUtil.get_formatted_percentage(image_count, total_count)
        image_size = NavUtil.calc_total_files_size(all_files, IMG_TAG)
        vid_count = NavUtil.get_type_count(all_files, VID_TAG)
        vid_perc = NavUtil.get_formatted_percentage(vid_count, total_count)
        vid_size = NavUtil.calc_total_files_size(all_files, VID_TAG)
        other_count = NavUtil.get_type_count(all_files, OTH_TAG)
        other_perc = NavUtil.get_formatted_percentage(other_count, total_count)
        other_size = NavUtil.calc_total_files_size(all_files, OTH_TAG)

        msg = "Total files= {0} Total Size= {1} GB".format(total_count, total_size)
        msg += "\nTotal duplicate files= {0}".format(NavUtil.get_type_count(duplicates))
        msg += "\nImage count= {0} ({1}%) size= {2} GB".format(image_count, image_perc, image_size)
        msg += "\nVideo count= {0} ({1}%) size= {2} GB".format(vid_count, vid_perc, vid_size)
        msg += "\nOther count= {0} ({1}%) size= {2} GB".format(other_count, other_perc, other_size)
        msg += "\nFile Name= {0}, Size= {1}, Type= {2}".format(all_files[0].get_filename(),
                                                            all_files[0].get_size(),
                                                            all_files[0].get_type())

        msg += "\nSize of all duplicates= {0} GB".format(NavUtil.calc_total_files_size(duplicates))
        EmailUtils.send_email(msg)
        print(msg)
