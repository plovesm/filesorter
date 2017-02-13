import unittest
from app import FileSorter
from objects import FSfile

START_DIR = r"/Users/paulottley/Desktop/Test_pics"
TGT_DIR = r"/Users/paulottley/Desktop/SortTarget"


class FileSorterTest(unittest.TestCase):

    def setUp(self):
        self.fs = FileSorter(START_DIR, TGT_DIR)

    def test_walk_dir(self):
        all_files = self.fs.walk_dir(START_DIR, TGT_DIR)
        self.assertEquals(17, len(all_files))

    def test_prepend_folder_name(self):
        file = FSfile()

        file.set_filename("2-PaulBaby.jpg")
        file.set_src_dir("/Users/paulottley/Desktop/MomsDadsPhotos/")

        updated_file = self.fs.prepend_folder_name(file)

        self.assertEquals("MomsDadsPhotos_2-PaulBaby.jpg", updated_file.get_tgt_filename())

        file2 = FSfile()

        file2.set_filename("2-PaulBaby.jpg")
        file2.set_src_dir("")
        updated_file2 = self.fs.prepend_folder_name(file2)

        self.assertEquals("2-PaulBaby.jpg", updated_file2.get_tgt_filename())

        file3 = FSfile()

        file3.set_filename("2-PaulBaby.jpg")
        file3.set_src_dir(None)
        updated_file3 = self.fs.prepend_folder_name(file3)

        self.assertEquals("2-PaulBaby.jpg", updated_file3.get_tgt_filename())

    """
    def test_mark_duplicates(self):
        all_files = self.fs.walk_dir(START_DIR, TGT_DIR)
        file_lists = self.fs.mark_duplicates(all_files)
        self.assertEquals(6, len(file_lists[1]))
        self.fs.final_report(file_lists)
    """

    def test_copy_files(self):
        all_files = self.fs.walk_dir(START_DIR, TGT_DIR)
        file_lists = self.fs.mark_duplicates(all_files)
        self.assertEquals(6, len(file_lists[1]))

        self.assertFalse(self.fs.copy_files(file_lists[0]))
        self.fs.final_report(file_lists)

    def test_merge_dir(self):
        all_files = self.fs.walk_dir(START_DIR, TGT_DIR)
        all_files2 = self.fs.walk_dir(r"/Users/paulottley/Desktop/Test_pics2", TGT_DIR)
        self.assertEquals(17, len(all_files))
        self.assertEquals(11, len(all_files2))

        file_lists = self.fs.merge_files(all_files, all_files2)
        for x in file_lists[0]:
            print("Name {0} and Size {1}".format(x.get_filename(), x.get_size()))
        print("Duplicates")
        for y in file_lists[1]:
            print("Name {0} and Size {1}".format(y.get_filename(), y.get_size()))
        self.assertEquals(19, len(file_lists[0]))
        self.assertEquals(9, len(file_lists[1]))

    """
    def test_sort_file(self):
        self.assertEquals("i", self.fs.sort_file("/Users/paulottley/img001.jpeg"))
        self.assertEquals("v", self.fs.sort_file("/Users/paulottley/img001.mov"))
        self.assertEquals("o", self.fs.sort_file("/Users/paulottley/img001.jp"))
        self.assertEquals("i", self.fs.sort_file("/Users/paulottley/img001.JPEG"))
        self.assertEquals("i", self.fs.sort_file("/Users/paulottley/img001.img.john.gif"))
        self.assertEquals("o", self.fs.sort_file(None))
        self.assertEquals("o", self.fs.sort_file(2))
    """
if __name__ == '__main__':
    unittest.main()
