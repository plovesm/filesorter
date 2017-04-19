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
