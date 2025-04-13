import unittest
from filters import filter_by_extensions


class TestFilterByExtension(unittest.TestCase):

    def test_content_no_match_extensions(self):
        filtered = filter_by_extensions([], [".pdf"])
        self.assertEqual(filtered, [])

    def test_content_match_extensions(self):
        filtered = filter_by_extensions(
            ["a.pdf", "c.docx", "b.pdf", "img.jpg", "folder", "test.pdf", "test.bmp"],
            [".pdf", ".docx"],
        )
        self.assertEqual(filtered, ["a.pdf", "c.docx", "b.pdf", "test.pdf"])
