
import unittest

class TestDemo(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testDemo(self):
        self.assertEquals((2 * 5), 10, "test num failed!")
        self.assertFalse(False, "test, boolen failed!")
        self.assertTrue(True, "test bool failed!")
        ss = "hello"
        self.assertEquals("hello", ss, "test string failed!")
