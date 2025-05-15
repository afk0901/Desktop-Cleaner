from filters import filter_by_extensions


class TestFilterByExtension:

    def test_content_no_match_extensions(self):
        filtered = filter_by_extensions([], [".pdf"])
        assert filtered == []

    def test_content_match_extensions(self):
        filtered = filter_by_extensions(
            ["a.pdf", "c.docx", "b.pdf", "img.jpg", "folder", "test.pdf", "test.bmp"],
            [".pdf", ".docx"],
        )
        assert filtered == ["a.pdf", "c.docx", "b.pdf", "test.pdf"]
