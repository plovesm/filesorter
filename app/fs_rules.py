# FileSorter
# @author Paul Ottley
# @copyright 2017

import os

"""
Constants
"""
SEPARATOR = os.sep
IMG_DIR = "images"
VID_DIR = "videos"
OTH_DIR = "other"
IMG_TAG = "i"
VID_TAG = "v"
OTH_TAG = "o"

MONTHS = {"Jan": "01",
          "Feb": "02",
          "Mar": "03",
          "Apr": "04",
          "May": "05",
          "Jun": "06",
          "Jul": "07",
          "Aug": "08",
          "Sep": "09",
          "Oct": "10",
          "Nov": "11",
          "Dec": "12"}

DATE_REGEX_WORD = r"(\w\w\w\s\d{1,2},\s(19|20)\d\d)"
DATE_REGEX_BASE = r"((19|20)\d\d[- /.:_]?(1[012]|0?[1-9])[- /.:_]?([12][0-9]|3[01]|0?[1-9]))"
DATE_REGEX = r"(^" + DATE_REGEX_BASE + ")|(\D" + DATE_REGEX_BASE + "\D)"
DATE_PREFIX_REGEX = DATE_REGEX + "[- /:_]?"

OLDEST_YEAR = 2002

DEBUG = False

IMG_TYPES = ["jpg", "png", "gif", "bmp", "jpeg", "nef", "tif"]
VID_TYPES = ["mpg", "mp4", "mpeg", "flv", "wmv", "mov", "avi", "3gp", "dv", "m4v"]


class Rules:

    @staticmethod
    def get_img_dir():
        return IMG_DIR

    @staticmethod
    def get_vid_dir():
        return VID_DIR

    @staticmethod
    def get_oth_dir():
        return OTH_DIR

    @staticmethod
    def get_img_tag():
        return IMG_TAG

    @staticmethod
    def get_vid_tag():
        return VID_TAG

    @staticmethod
    def get_oth_tag():
        return OTH_TAG

    @staticmethod
    def get_img_types():
        return IMG_TYPES

    @staticmethod
    def get_vid_types():
        return VID_TYPES

    @staticmethod
    def get_debug():
        return DEBUG

    @staticmethod
    def get_date_regex():
        return DATE_REGEX

    @staticmethod
    def get_date_regex_prefix():
        return DATE_PREFIX_REGEX

    @staticmethod
    def get_date_regex_word():
        return DATE_REGEX_WORD

    @staticmethod
    def get_months_list():
        return MONTHS

    @staticmethod
    def get_oldest_year():
        return OLDEST_YEAR
