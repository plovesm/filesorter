# FileSorter
# @author Paul Ottley
# @copyright 2017
import os

from decimal import Decimal

from app import EmailUtils

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
        total_count = ReportUtil.get_type_count(all_files)
        total_size = ReportUtil.calc_total_files_size(all_files)
        image_count = ReportUtil.get_type_count(all_files, IMG_TAG)
        image_perc = ReportUtil.get_formatted_percentage(image_count, total_count)
        image_size = ReportUtil.calc_total_files_size(all_files, IMG_TAG)
        vid_count = ReportUtil.get_type_count(all_files, VID_TAG)
        vid_perc = ReportUtil.get_formatted_percentage(vid_count, total_count)
        vid_size = ReportUtil.calc_total_files_size(all_files, VID_TAG)
        other_count = ReportUtil.get_type_count(all_files, OTH_TAG)
        other_perc = ReportUtil.get_formatted_percentage(other_count, total_count)
        other_size = ReportUtil.calc_total_files_size(all_files, OTH_TAG)

        msg = "Total files= {0} Total Size= {1} GB".format(total_count, total_size)
        msg += "\nTotal duplicate files= {0}".format(ReportUtil.get_type_count(duplicates))
        msg += "\nImage count= {0} ({1}%) size= {2} GB".format(image_count, image_perc, image_size)
        msg += "\nVideo count= {0} ({1}%) size= {2} GB".format(vid_count, vid_perc, vid_size)
        msg += "\nOther count= {0} ({1}%) size= {2} GB".format(other_count, other_perc, other_size)
        msg += "\nFile Name= {0}, Size= {1}, Type= {2}".format(all_files[0].get_filename(),
                                                               all_files[0].get_size(),
                                                               all_files[0].get_type())

        msg += "\nSize of all duplicates= {0} GB".format(ReportUtil.calc_total_files_size(duplicates))
        EmailUtils.send_email(msg)
        print(msg)

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

            return ReportUtil.format_four_places(total_size / 1000000000)
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
    def get_formatted_percentage(numerator, denominator):
        return ReportUtil.format_four_places((numerator / denominator) * 100)
