import unittest
from gencontent import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_title_extract_1(self):
        actual = extract_title("# This is just a test")
        self.assertEqual(actual, "This is just a test")

    def test_title_extract_2(self):
        actual = extract_title(
            """
# This should also appear

# Supposedly this won't appear
"""
        )
        self.assertEqual(actual, "This should also appear")
    
    def test_title_extract_3(self):
        actual = extract_title(
            """
Would this appear

# If I do the title after it

But this should make it clear 
"""
        )
        self.assertEqual(actual, "If I do the title after it")

    def test_title_extract_4(self):
        actual = extract_title("So this shouldn't work if i dont give it a title, right?")
        self.assertNotEqual(actual, "This is just a stand-in")

    def test_title_extract_5(self):
        actual = extract_title("# Could I write all the titles on one line\nBut does this mess anything up?")
        self.assertEqual(actual, "Could I write all the titles on one line")