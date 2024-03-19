import unittest
import util


class TestUtil(unittest.TestCase):

    def test_get_day_monday(self):
        day = util.get_day("2024-03-11")
        self.assertEqual("Monday", day)

    def test_get_day_tuesday(self):
        day = util.get_day("2024-03-12")
        self.assertEqual("Tuesday", day)

    def test_get_day_wednesday(self):
        day = util.get_day("2024-03-13")
        self.assertEqual("Wednesday", day)

    def test_get_day_thursday(self):
        day = util.get_day("2024-03-14")
        self.assertEqual("Thursday", day)

    def test_get_day_friday(self):
        day = util.get_day("2024-03-15")
        self.assertEqual("Friday", day)

    def test_get_day_saturday(self):
        day = util.get_day("2024-03-16")
        self.assertEqual("Saturday", day)

    def test_get_day_sunday(self):
        day = util.get_day("2024-03-17")
        self.assertEqual("Sunday", day)


    def test_get_month(self):
        self.assertEqual("January", util.get_month("2024-01-17"))
        self.assertEqual("February", util.get_month("2024-02-17"))
        self.assertEqual("March", util.get_month("2024-03-17"))
        self.assertEqual("November", util.get_month("2024-11-17"))
        self.assertEqual("December", util.get_month("2024-12-17"))

    def test_uv_index_low(self):
        index = util.get_uv_index_rate(1.0)
        self.assertTrue("Low" in index)
        index = util.get_uv_index_rate(2.0)
        self.assertTrue("Low" in index)

    def test_uv_index_moderate(self):
        index = util.get_uv_index_rate(3.0)
        self.assertTrue("Moderate" in index)
        index = util.get_uv_index_rate(4.0)
        self.assertTrue("Moderate" in index)
        index = util.get_uv_index_rate(5.0)
        self.assertTrue("Moderate" in index)
        
    def test_uv_index_high(self):
        index = util.get_uv_index_rate(6.0)
        self.assertTrue("High" in index)
        index = util.get_uv_index_rate(7.0)
        self.assertTrue("High" in index)
        
    def test_get_uv_index_very_high(self):
        index = util.get_uv_index_rate(8.0)
        self.assertTrue("Very High" in index)
        index = util.get_uv_index_rate(9.0)
        self.assertTrue("Very High" in index)
        index = util.get_uv_index_rate(10.0)
        self.assertTrue("Very High" in index)
        

    def test_uv_index_extreme(self):
        index = util.get_uv_index_rate(11.0)
        self.assertTrue("Extreme" in index)
        index = util.get_uv_index_rate(12.0)
        self.assertTrue("Extreme" in index)
        
        