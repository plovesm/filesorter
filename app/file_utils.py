# FileUtils
# @author Paul Ottley
# @copyright 2017
import hashlib
import os
import sys
from shutil import copyfile
from shutil import move


class FileUtils:

    # Return the file type after the dot
    @staticmethod
    def get_file_type(filename):
        # Guilty until proven innocent
        file_type = "unrecognized"

        # Grab the substring after the last dot and update file_type if found
        try:
            t = str.lower(filename.rpartition(".")[2])

            # If the outcome is not the same as the input, then we were able to pull a file type
            if filename != t:
                file_type = t

        except AttributeError:
            file_type = "error"

        return file_type

    @staticmethod
    def move_file(src_f, tgt_dir, tgt_filename):
        # Move files to image, video, other
        try:
            if FileUtils.does_file_exist(tgt_filename, tgt_dir):
                return FileUtils.move_file(src_f, tgt_dir, FileUtils.rename_file(tgt_filename, "((d))"))

            move(src_f, tgt_dir + tgt_filename)
        except FileNotFoundError:
            print("Err: Could not move to that location. Creating folder...")
            if not os.path.exists(tgt_dir):
                os.mkdir(tgt_dir)
                return FileUtils.move_file(src_f, tgt_dir, tgt_filename)

        return False

    @staticmethod
    def copy_file(src_f, tgt_dir, tgt_filename):
        print("Copying File: " + tgt_dir + tgt_filename)
        # Copy files to target destination
        try:
            if FileUtils.does_file_exist(tgt_filename, tgt_dir):
                # TODO figure out a way to identify same name before copy (Identify in mark duplicates)
                return FileUtils.copy_file(src_f, tgt_dir, FileUtils.rename_file(tgt_filename, "((d))"))

            copyfile(src_f, tgt_dir + tgt_filename)
        except FileNotFoundError:
            print("Err: Could not copy to that location. Creating folder...")

            if not os.path.exists(tgt_dir):
                os.makedirs(tgt_dir)
                return FileUtils.copy_file(src_f, tgt_dir, tgt_filename)

        return False

    @staticmethod
    def does_file_exist(filename, tgt_dir):
        return os.path.isfile(str(tgt_dir)+str(filename))

    @staticmethod
    def rename_file(filename, suffix):
        # Split the file name on the last "."
        filename_arr = filename.rpartition(".")
        # Append the suffix
        return "{0}{1}{2}{3}".format(filename_arr[0], suffix, filename_arr[1], filename_arr[2])

    @staticmethod
    def is_file_dup(file1, file2):
        # Check if file exists
        if FileUtils.does_file_exist(file1, "") and FileUtils.does_file_exist(file2, ""):
            # Check file size first
            return os.path.getsize(file1) == os.path.getsize(file2) and FileUtils.hash_file(file1) == FileUtils.hash_file(file2)

        # If we get to this point, a file either doesn't exist or it didn't match
        return False

    @staticmethod
    def get_file_size(f):
        return os.path.getsize(f)

    @staticmethod
    def hash_file(file):
        if FileUtils.does_file_exist(file, ""):
            block_size = 65536
            hasher = hashlib.md5()
            with open(file, 'rb') as a_file:
                buf = a_file.read(block_size)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = a_file.read(block_size)
            return hasher.hexdigest()
        else:
            return "file doesn't exist"

    @staticmethod
    def delete_file():
        return

    @staticmethod
    def compare_file():
        return
