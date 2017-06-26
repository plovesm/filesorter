import unittest
from app import ImageUtils


class ImageUtilsTest(unittest.TestCase):
    def test_get_dt_captured(self):
        self.assertEqual("1992:03:01 00:00:00", ImageUtils.get_original_date(
            "/Users/paulottley/Desktop/SortSource/Ottley_Home_Movies_19920301_3.mp4"), "1900 check")

        self.assertEqual("2017:04:14 00:51:40", ImageUtils.get_original_date(
                            "/Users/paulottley/Desktop/SortSource/IMG_4739.JPG"), "Happy Path")

        self.assertEqual("0000:00:00 00:00:00", ImageUtils.get_original_date(
            "/Users/paulottley/Desktop/SortSource/images_images_09-September_New_Malibu.JPG"), "Malibu check")

        self.assertEqual("2013-05-17 18:04:48", ImageUtils.get_original_date(
            "/Users/paulottley/Desktop/SortSource/Family_VID_20130517_130427.3gp"), "3gp check")

        self.assertEqual("2012-09-25 19:40:24", ImageUtils.get_original_date(
            "/Users/paulottley/Desktop/SortSource/videos_videos_Family_IMG_0063.MOV"), "MOV check")

    def test_remove_false_timestamp(self):
        test_name = "20150803-042006_20150505_221117_LLS.jpg"

        self.assertEqual("042006_20150505_221117_LLS.jpg", ImageUtils.remove_false_datestamp(test_name))

        test_name = "042006_20150803-20150505_221117_LLS.jpg"

        self.assertEqual("042006_20150803-20150505_221117_LLS.jpg", ImageUtils.remove_false_datestamp(test_name))

        test_name = "20150803-042006_20150505-221117_LLS.jpg"

        self.assertEqual("042006_20150505-221117_LLS.jpg", ImageUtils.remove_false_datestamp(test_name))

    def test_get_dt_from_filename(self):

        self.assertEqual("2013-09-23", ImageUtils.get_dt_from_name("video_Family_2013-09-23-09-36-45.mov"), "Test 1")
        self.assertEqual("2013-09-23", ImageUtils.get_dt_from_name("video_Family_2013-9-23-09-36-45.mov"), "Test 2")
        self.assertEqual("2013-09-03", ImageUtils.get_dt_from_name("video_Apr 4, 2014_Family_2013-9-3.mov")[1], "Test 3")
        self.assertEqual("2013-09-03", ImageUtils.get_dt_from_name("video_Family_2013-9-03.mov")[1], "Test 4")
        self.assertEqual("2013-09-03", ImageUtils.get_dt_from_name("video_222012062356045_Family_2013-09-3.mov")[1], "Test 5")
        self.assertEqual("2013-10-09", ImageUtils.get_dt_from_name("video_Family_2013-10-9.mov")[1], "Test 6")
        self.assertEqual("2013-11-23", ImageUtils.get_dt_from_name("video_Family_2013-11-23.mov")[1], "Test 7")
        self.assertEqual("2013-09-13", ImageUtils.get_dt_from_name("video_Family_2013-9-13.mov")[1], "Test 8")
        self.assertEqual("2013-09-23", ImageUtils.get_dt_from_name("video_Family_2013-09-23-09-36-45.3gp")[1], "Test 9")
        self.assertEqual(None, ImageUtils.get_dt_from_name("video_Family_10334467.3gp")[1], "Test 10")
        self.assertEqual(None, ImageUtils.get_dt_from_name("video_Family_19334467.3gp")[1], "Test 11")
        self.assertEqual("2013-06-07", ImageUtils.get_dt_from_name("video.Family.2013.06.07.mov")[1], "Test 12")
        self.assertEqual("2010-09-07", ImageUtils.get_dt_from_name("video_Family_20100907_family.mp4")[1], "Test 13")
        self.assertEqual(None, ImageUtils.get_dt_from_name("video_Family_19330907_family.mp4")[1], "Test 14")
        self.assertEqual("2003-11-12", ImageUtils.get_dt_from_name("20031112_.3gp")[1], "Test 15")
        self.assertEqual(None, ImageUtils.get_dt_from_name("")[1], "Test 16")
        self.assertEqual(None, ImageUtils.get_dt_from_name(None)[1], "Test 17")
        self.assertEqual(None, ImageUtils.get_dt_from_name("Megan and Emily Visit_P5020066_1.MOV")[1], "False positive")
        self.assertEqual(None, ImageUtils.get_dt_from_name(2)[1], "Test 18")
        self.assertEqual("2010-09-07", ImageUtils.get_dt_from_name("video_Family_2010:09:07_family.mp4")[1], "Test 19")
        self.assertEqual(None, ImageUtils.get_dt_from_name("Frog")[1], "Test 20")
        self.assertEqual("2012-12-20", ImageUtils.get_dt_from_name("2002-12-08_20161112-00-20140535-4825_IMG_20121220_112808.jpg")[1], "Test 21")

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

        dt3 = ImageUtils.get_dt_captured_split("0000:00:00 00:00:00")

        self.assertEqual(1900, dt3.year)
        self.assertEqual(1, dt3.month)
        """
        shouldbeerror = ImageUtils.get_dt_captured_split("0B:00:00")
        self.assertIsInstance(shouldbeerror, ValueError)

        shouldbeerror = ImageUtils.get_dt_captured_split(None)
        self.assertIsInstance(shouldbeerror, Exception)

        shouldbeerror = ImageUtils.get_dt_captured_split("")
        self.assertIsInstance(shouldbeerror, IndexError)

        shouldbeerror = ImageUtils.get_dt_captured_split("frog lips")
        self.assertIsInstance(shouldbeerror, ValueError)
        """
    def test_get_dimensions(self):
        self.assertEqual("3264x2448", ImageUtils.get_dimensions(
                            "/Users/paulottley/Google Drive/MomsDadsPhotos/IMG_0002.jpg"))

    def test_set_date(self):
        self.assertEqual("0000:00:00 00:00:00", ImageUtils.get_dt_captured(
            "/Users/paulottley/Desktop/SortSource/Family_VID_20130517_130053.mp4"), "mp4 check")

        ImageUtils.set_date("/Users/paulottley/Desktop/SortSource/Family_VID_20130517_130218.mp4", 2013, 5, 17)

        self.assertEqual("2013:05:17 18:04:48", ImageUtils.get_dt_captured(
            "/Users/paulottley/Desktop/SortSource/Family_VID_20130517_130218.mp4"), "mp4 check")


if __name__ == '__main__':
    unittest.main()
