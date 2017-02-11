import unittest
from app import FileUtils

class FileUtilsTest(unittest.TestCase):

    def test_get_file_type(self):
        self.assertEquals("jpg", FileUtils.get_file_type("img001.jpg"))
        self.assertEquals("jpeg", FileUtils.get_file_type("img001.JPeg"))
        self.assertEquals("jpg", FileUtils.get_file_type("img001.JPG"))
        self.assertEquals("jpg", FileUtils.get_file_type("img.001.JPG"))
        self.assertEquals("unrecognized", FileUtils.get_file_type("img001"))
        self.assertEquals("thisisareallylongfileextension",
                          FileUtils.get_file_type("img001.thisisareallylongfileextension"))
        self.assertEquals("unrecognized", FileUtils.get_file_type(""))
        self.assertEquals("error", FileUtils.get_file_type(None))
        self.assertEquals("error", FileUtils.get_file_type(2))

    def test_copy_file(self):
        self.assertFalse(FileUtils.copy_file("/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0001.jpg",
                                             "/Users/paulottley/Desktop/SortTarget/images/", "IMG_0001.jpg"))
        self.assertFalse(FileUtils.copy_file("/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0001.jpg",
                                             "/Users/paulottley/Desktop/SortTarget/frog/", "IMG_0001.jpg"))

    # def test_move_file(self):
    #    self.assertFalse(FileUtils.move_file("/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0001.jpg",
    #                                         "/Users/paulottley/Desktop/SortTarget/images/", "IMG_0001.jpg"))

    def test_does_file_exist(self):
        self.assertFalse(FileUtils.does_file_exist("fakefile", " "))
        self.assertFalse(FileUtils.does_file_exist(2, " "))
        self.assertTrue(FileUtils.does_file_exist("IMG_0001.jpg", "/Users/paulottley/Desktop/MomsDadsPhotos/"))

    def test_is_file_dup(self):
        self.assertTrue(FileUtils.is_file_dup("/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0001.jpg",
                                              "/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0001 copy.jpg"))
        self.assertFalse(FileUtils.is_file_dup("/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0001.jpg",
                                               "/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0002.jpg"))
        self.assertFalse(FileUtils.is_file_dup("/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0001.jpg",
                                               2))
        self.assertFalse(FileUtils.is_file_dup(None, "/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0001.jpg"))
        self.assertFalse(FileUtils.is_file_dup("", "/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0001.jpg"))
        self.assertFalse(FileUtils.is_file_dup("/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0718.jpg",
                                               "/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0730.jpg"))
        self.assertFalse(FileUtils.is_file_dup("/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0001.jpg",
                                               "/Users/paulottley/Desktop/MomsDadsPhotos/images/IMG_0001.jpg"))

    def test_rename_file(self):
        self.assertEquals("IMG_0001-dup.jpg", FileUtils.rename_file("IMG_0001.jpg", "-dup"))
        self.assertEquals("IMG_0001None.jpg", FileUtils.rename_file("IMG_0001.jpg", None))
        self.assertEquals("IMG_00012.jpg", FileUtils.rename_file("IMG_0001.jpg", 2))

    def test_hash_file(self):
        self.assertEquals("84365b010f4d772abbc275d8128bfa26",
                          FileUtils.hash_file("/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0001.jpg"))
        self.assertEquals("84365b010f4d772abbc275d8128bfa26",
                          FileUtils.hash_file("/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0001 copy.jpg"))
        self.assertEquals("file doesn't exist",
                          FileUtils.hash_file(2))
        self.assertEquals("file doesn't exist",
                          FileUtils.hash_file(None))

if __name__ == '__main__':
    unittest.main()
