from pathlib import Path
import shutil


class setUpTearDown:

    def __init__(self):
        self.test_dir = Path("test_temp")

    def get_test_dir_path(self):
        return self.test_dir

    def get_source_dir_path(self):
        return self.test_dir

    def get_destination_dir_name(self):
        return "destination"

    def get_destination_dir_path(self):
        return self.test_dir / self.get_destination_dir_name()

    def get_source_directory_content(self):
        return [
            "test_file1.jpg",
            "test_file2.png",
            "test_file4.docx",
            "test_file5.jpeg",
            "test_file3.txt",
            "test_file9.pdf",
            "test_file6.webp",
            "test_file0.doc",
            "test_file10.odt",
            "test_file12.csv",
            "test_file2.xlsx",
            "test_file7.bmp",
        ]

    def initialize_test_dir(
        self, source_directory_path: str, source_directory_content: list = None
    ):

        for file_name in source_directory_content:
            file_path = Path(source_directory_path) / file_name
            file_path.touch()

    def setup(self):
        Path(self.get_test_dir_path()).mkdir(exist_ok=True)
        Path(self.get_destination_dir_path()).mkdir(exist_ok=True)

    def teardown(self):
        shutil.rmtree(self.get_test_dir_path())
