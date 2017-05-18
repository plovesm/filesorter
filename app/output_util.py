# copyright 2017
# author Paul Ottley


class OutputUtil:
    @staticmethod
    def open_file(fn):
        file = open(fn, "rw+")
        return file

    @staticmethod
    def write_to_file(str_line):
        print(str_line)

    @staticmethod
    def close_file(file):
        file.close()