from desktop_organizer import create_directory_by_filtered_directory_content
from pathlib import Path
import os
import shutil


class TestCreateDirectoryByFilteredDirectoryContent:

    def setup_method(self):
        os.mkdir("./test_source_directory")
        self.source_dir = Path("test_source_directory")
        self.new_dir = Path("test_source_directory") / Path("new_directory")

    def teardown_method(self):
        shutil.rmtree(self.source_dir)

    def test_create_directory_when_filtered_directory_content_not_empty(self):
        create_directory_by_filtered_directory_content(
            source_directory_path="test_source_directory",
            filtered_directory_content=["file1.txt", "file2.txt"],
            new_directory_name="new_directory",
        )
        assert self.new_dir.exists()

    def test_do_not_create_directory_when_filtered_directory_content_empty(self):
        create_directory_by_filtered_directory_content(
            source_directory_path="test_source_directory",
            filtered_directory_content=[],
            new_directory_name="new_directory",
        )
        assert not self.new_dir.exists()
