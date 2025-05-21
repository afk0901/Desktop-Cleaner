from tests.set_up_tear_down import setUpTearDown
from move import move_multiple_files_by_dir_contents
from unittest.mock import patch


class TestMoveMultipleFilesByDirContents:

    def setup_method(self):
        self.setup_teardown = setUpTearDown()
        self.setup_teardown.setup()
        self.source_dir = self.setup_teardown.get_source_dir_path()
        self.new_directory_name = self.setup_teardown.get_destination_dir_name()

    def teardown_method(self):
        self.setup_teardown = setUpTearDown()
        self.setup_teardown.teardown()

    @patch("move._safe_move")
    def test_successful_move_multiple_files(self, safe_move_mock):

        directory_content = [
            "file1.txt",
            "file2.txt",
            "file3.jpg",
            "subdir1",
            "subdir2",
        ]

        move_multiple_files_by_dir_contents(
            self.source_dir,
            self.new_directory_name,
            directory_content,
        )

        assert safe_move_mock.call_count == len(directory_content)

    @patch("move._safe_move")
    def test_successful_move_multiple_files_only_folders(self, safe_move_mock):

        directory_content = [
            "subdir1",
            "subdir2",
        ]

        move_multiple_files_by_dir_contents(
            self.source_dir,
            self.new_directory_name,
            directory_content,
        )

        assert safe_move_mock.call_count == 2

    @patch("move._safe_move")
    def test_successful_move_multiple_files_with_empty_directory_content(
        self, safe_move_mock
    ):

        directory_content = []

        move_multiple_files = move_multiple_files_by_dir_contents(
            self.source_dir,
            self.new_directory_name,
            directory_content,
        )

        assert safe_move_mock.call_count == 0
        assert move_multiple_files == None
