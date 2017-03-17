import unittest
from app import ImageUtils


class ImageUtilsTest(unittest.TestCase):
    def test_get_dt_captured(self):
        self.assertEqual("2014:11:26 09:55:12", ImageUtils.get_dt_captured(
                            "/Users/paulottley/Google Drive/MomsDadsPhotos/IMG_0002.jpg"))

    def test_get_dt_captured_video(self):
        self.assertEqual("fjk", ImageUtils.get_dt_captured(
                            "/Users/paulottley/Google Drive/MomsDadsPhotos/IMG_0263.MOV"))

    def test_get_vid_metadata(self):
        self.assertEqual("fjk", ImageUtils.get_vid_metadata(
                            "/Users/paulottley/Google Drive/MomsDadsPhotos/IMG_0263.MOV"))

    def test_get_dt_captured_split(self):
        dt_arr = ImageUtils.get_dt_captured_split(
            "/Users/paulottley/Google Drive/MomsDadsPhotos/IMG_0002.jpg")

        self.assertEqual("2014", dt_arr[0])
        self.assertEqual("11", dt_arr[1])

    def test_get_dimensions(self):
        self.assertEqual("3264x2448", ImageUtils.get_dimensions(
                            "/Users/paulottley/Google Drive/MomsDadsPhotos/IMG_0002.jpg"))


if __name__ == '__main__':
    unittest.main()
