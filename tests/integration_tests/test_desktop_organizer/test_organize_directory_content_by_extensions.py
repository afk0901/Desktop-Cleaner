from desktop_organizer import _organize_directory_content_by_extensions
import os
from pathlib import Path
from tests.set_up_tear_down import setUpTearDown


class TestOrganizeDirectoryContentByExtensions:

    def setup_method(self):
        setup_tear_down = setUpTearDown()
        os.mkdir(setup_tear_down.get_test_dir_path())
        self.source_directory_path = setup_tear_down.get_test_dir_path()
        self.source_directory_content = setup_tear_down.get_source_directory_content()
        setup_tear_down.initialize_test_dir(self.source_directory_path, 
                                            self.source_directory_content)

    def teardown_method(self):
        setUpTearDown().teardown()

    def test_organize_directory_content_by_extensions(self):
        _organize_directory_content_by_extensions(
            self.source_directory_path,
            self.source_directory_content,
            "images",
            [".jpg", ".jpeg", ".png", ".webp", ".bmp"],
        )
        new_dir = Path(self.source_directory_path) / Path("images")
        new_dir_content = os.listdir(new_dir)
        assert new_dir_content.sort() == [
            "test_file1.jpg",
            "test_file2.png",
            "test_file5.jpeg",
            "test_file6.webp",
            "test_file7.bmp",
        ].sort()
