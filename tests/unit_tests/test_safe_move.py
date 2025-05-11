from tests.set_up_tear_down import setUpTearDown
from unittest.mock import patch
from move import _safe_move


class TestSafeMove:
    def setup_method(self):
        self.setup_teardown = setUpTearDown()
        self.setup_teardown.setup()
        self.source_dir = self.setup_teardown.get_source_dir_path()
        self.destination_dir_name = self.setup_teardown.get_destination_dir_name()

    def teardown_method(self):
        self.setup_teardown = setUpTearDown()
        self.setup_teardown.teardown()

    @patch("move._move_file")
    def test_safe_move_file_successful(self, move_file_mock):

        _safe_move(self.source_dir, self.destination_dir_name, "test_file.txt")
        assert move_file_mock.call_count == 1

    @patch("move._move_file", side_effect=PermissionError)
    def test_safe_move_permission_should_not_raise_permission_error(
        self, move_file_mock
    ):

        _safe_move(self.source_dir, self.destination_dir_name, "test_file.txt")

    @patch("move._move_file", side_effect=Exception)
    def test_safe_move_should_not_raise_unexpected_error(self, move_file_mock):

        _safe_move(self.source_dir, self.destination_dir_name, "test_file.txt")
