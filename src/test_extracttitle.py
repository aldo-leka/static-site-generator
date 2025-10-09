import unittest

from extracttitle import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extracttitle1(self):
        self.assertEqual("World", extract_title("\n\nHello\n# World\n\n# ,right?"))

    def test_extracttitle2(self):
        with self.assertRaises(Exception):
            extract_title("#TEST")

    def test_extracttitle3(self):
        self.assertEqual("World", extract_title("\n\nHello\n# World   \n\n# ,right?"))