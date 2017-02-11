import unittest
from app import FileSorter

START_DIR = r"/Users/paulottley/Desktop/Test_pics"
TGT_DIR = r"/Users/paulottley/Desktop/SortTarget"


class FileSorterTest(unittest.TestCase):

    def setUp(self):
        self.fs = FileSorter(START_DIR, TGT_DIR)

    def test_walk_dir(self):
        all_files = self.fs.walk_dir(START_DIR, TGT_DIR)
        self.assertEquals(17, len(all_files))

    # def test_mark_duplicates(self):
    #    all_files = self.fs.walk_dir(START_DIR, TGT_DIR)
    #    file_lists = self.fs.mark_duplicates(all_files)
    #    self.assertEquals(6, len(file_lists[1]))
    #    self.fs.final_report(file_lists)

    def test_copy_files(self):
        all_files = self.fs.walk_dir(START_DIR, TGT_DIR)
        file_lists = self.fs.mark_duplicates(all_files)
        self.assertEquals(6, len(file_lists[1]))
        print("All Files")
        for x in file_lists[0]:
            print(x.get_filename())
        print("Duplicates")
        for y in file_lists[1]:
            print(y.get_filename())
        # self.assertFalse(self.fs.copy_files(file_lists[0]))
        self.fs.final_report(file_lists)

    def test_merge_dir(self):
        all_files = self.fs.walk_dir(START_DIR, TGT_DIR)
        all_files2 = self.fs.walk_dir(r"/Users/paulottley/Desktop/Test_pics2", TGT_DIR)
        self.assertEquals(17, len(all_files))
        self.assertEquals(11, len(all_files2))

        file_lists = self.fs.mark_duplicates(all_files, all_files2)

        self.assertEquals(18, len(file_lists[0]))
        self.assertEquals(8, len(file_lists[1]))

    # def test_sort_file(self):
    #     self.assertEquals("i", self.fs.sort_file("/Users/paulottley/img001.jpeg"))
    #     self.assertEquals("v", self.fs.sort_file("/Users/paulottley/img001.mov"))
    #     self.assertEquals("o", self.fs.sort_file("/Users/paulottley/img001.jp"))
    #     self.assertEquals("i", self.fs.sort_file("/Users/paulottley/img001.JPEG"))
    #     self.assertEquals("i", self.fs.sort_file("/Users/paulottley/img001.img.john.gif"))
    #     self.assertEquals("o", self.fs.sort_file(None))
    #     self.assertEquals("o", self.fs.sort_file(2))

if __name__ == '__main__':
    unittest.main()
