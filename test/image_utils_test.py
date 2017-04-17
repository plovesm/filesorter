import unittest
from app import ImageUtils


class ImageUtilsTest(unittest.TestCase):
    def test_get_dt_captured(self):
        self.assertEqual("2017:04:14 00:51:40", ImageUtils.get_dt_captured(
                            "/Users/paulottley/Desktop/SortSource/IMG_4739.JPG"), "Happy Path")

        self.assertEqual("0000:00:00 00:00:00", ImageUtils.get_dt_captured(
            "/Users/paulottley/Desktop/SortSource/images_images_09-September_New_Malibu.JPG"), "Malibu check")

        self.assertEqual("2013-05-17 18:04:48", ImageUtils.get_dt_captured(
            "/Users/paulottley/Desktop/SortSource/Family_VID_20130517_130427.3gp"), "3gp check")

        self.assertEqual("2012-09-25 19:40:24", ImageUtils.get_dt_captured(
            "/Users/paulottley/Desktop/SortSource/videos_videos_Family_IMG_0063.MOV"), "MOV check")

    def test_get_dt_captured_bad_file(self):
        self.assertEqual("00:00:00", ImageUtils.get_dt_captured(
                            "/Users/paulottley/Desktop/SortSource/images_images_09-September_New_Malibu.JPG"))

    def test_get_dt_captured_video(self):
        self.assertEqual("2012-06-06 18:47:57", ImageUtils.get_dt_captured(
                            "/Users/paulottley/Google Drive/MomsDadsPhotos/IMG_0263.MOV"))

    def test_get_vid_metadata(self):
        self.assertEqual("2017:03:17", ImageUtils.get_alt_metadata(
            "/Users/paulottley/Desktop/SortTarget/videos/0M/00/videos_20161107-021757_IMG_0942.mp4"))

    def test_get_dt_captured_split(self):
        dt = ImageUtils.get_dt_captured_split("2014:05:23 10:23:32")

        self.assertEqual(2014, dt.year)
        self.assertEqual(5, dt.month)

        dt2 = ImageUtils.get_dt_captured_split("2014:05:23")

        self.assertEqual(2014, dt2.year)
        self.assertEqual(5, dt2.month)

        dt3 = ImageUtils.get_dt_captured_split("2012-06-06 18:47:57")

        self.assertEqual(2012, dt3.year)
        self.assertEqual(6, dt3.month)

        shouldbeerror = ImageUtils.get_dt_captured_split("0B:00:00")
        self.assertIsInstance(shouldbeerror, ValueError)

        shouldbeerror = ImageUtils.get_dt_captured_split(None)
        self.assertIsInstance(shouldbeerror, Exception)

        shouldbeerror = ImageUtils.get_dt_captured_split("")
        self.assertIsInstance(shouldbeerror, IndexError)

        shouldbeerror = ImageUtils.get_dt_captured_split("frog lips")
        self.assertIsInstance(shouldbeerror, ValueError)

    def test_get_dimensions(self):
        self.assertEqual("3264x2448", ImageUtils.get_dimensions(
                            "/Users/paulottley/Google Drive/MomsDadsPhotos/IMG_0002.jpg"))


if __name__ == '__main__':
    unittest.main()
