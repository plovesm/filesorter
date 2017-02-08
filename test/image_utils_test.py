import unittest
from app import ImageUtils

class ImageUtilsTest(unittest.TestCase):
    def test_get_dt_captured(self):
        self.assertEqual("2014:11:26 09:55:12", ImageUtils.get_dt_captured("/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0002.jpg"))

    def test_get_dimensions(self):
        self.assertEqual("3264x2448", ImageUtils.get_dimensions("/Users/paulottley/Desktop/MomsDadsPhotos/IMG_0002.jpg"))


if __name__ == '__main__':
    unittest.main()
