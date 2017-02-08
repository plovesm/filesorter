# FSfile
# @author Paul Ottley
# @copyright 2017


class FSfile:

    def __init__(self):
        self._filename = ""
        self._src_dir = ""
        self._tgt_dir = ""
        self._tgt_folder = ""
        self._tgt_filename = ""
        self._type = ""
        self._size = 0
        self._date_taken = ""

    def get_filename(self):
        return self._filename

    def set_filename(self, filename):
        self._filename = filename

    def get_tgt_filename(self):
        if self._tgt_filename is "":
            return self._filename

        return self._tgt_filename

    def set_tgt_filename(self, filename):
        self._tgt_filename = filename

    def get_full_path(self):
        return self._src_dir + self._filename

    def get_full_tgt_path(self):
        return self._tgt_dir + self._tgt_folder + self._tgt_filename

    def get_src_dir(self):
        return self._src_dir

    def set_src_dir(self, src_dir):
        self._src_dir = src_dir

    def get_tgt_dir(self):
        return self._tgt_dir

    def set_tgt_dir(self, tgt_dir):
        self._tgt_dir = tgt_dir

    def get_tgt_folder(self):
        return self._tgt_folder

    def set_tgt_folder(self, tgt_folder):
        self._tgt_folder = tgt_folder

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def get_size(self):
        return self._size

    def set_size(self, size):
        self._size = size

    def get_date_taken(self):
        return self._date_taken

    def set_date_taken(self, date_taken):
        self._date_taken = date_taken
