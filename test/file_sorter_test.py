import unittest
from app import FileSorter


class FileSorterTest(unittest.TestCase):

    def setUp(self):
        self.fs = FileSorter(r"/Users/paulottley/Desktop/Test_pics", r"/Users/paulottley/Desktop/SortTarget")

    def test_walk_dir(self):
        self.fs.walk_dir("")
        self.assertEquals(15, len(self.fs.all_files))

    def test_mark_duplicates(self):
        self.test_walk_dir()
        self.fs.mark_duplicates()
        self.assertEquals(6, len(self.fs.duplicates))
        self.fs.final_report()

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
