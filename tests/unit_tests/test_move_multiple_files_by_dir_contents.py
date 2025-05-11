from tests.move_set_up_tear_down import setUpTearDown
from move import move_multiple_files_by_dir_contents
from unittest.mock import patch


class TestMoveMultipleFilesByDirContents:

    def setup_method(self):
        self.setup_teardown = setUpTearDown()
        self.setup_teardown.setup()
        self.source_dir = self.setup_teardown.get_source_dir_path()
        self.new_directory_name = self.setup_teardown.get_destination_dir_name()
        self.directory_content = [
            "file1.txt",
            "file2.txt",
            "file3.jpg",
            "subdir1",
            "subdir2",
        ]

    def teardown_method(self):
        self.setup_teardown = setUpTearDown()
        self.setup_teardown.teardown()

    @patch("move._safe_move")
    def test_successful_move_multiple_files(self, safe_move_mock):

        move_multiple_files_by_dir_contents(
            self.source_dir,
            self.new_directory_name,
            self.directory_content,
        )

        assert safe_move_mock.call_count == len(self.directory_content)
