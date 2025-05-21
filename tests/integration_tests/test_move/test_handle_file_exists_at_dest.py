from move import _handle_file_exists_at_dest
from tests.set_up_tear_down import setUpTearDown


class TestHandleFileExistsAtDest:

    def setup_method(self):
        self.setup_teardown = setUpTearDown()
        self.setup_teardown.setup()
        self.source_dir = self.setup_teardown.get_source_dir_path()
        self.destination_dir = self.setup_teardown.get_destination_dir_path()

    def teardown_method(self):
        self.setup_teardown = setUpTearDown()
        self.setup_teardown.teardown()

    def test_handle_file_exists_at_dest_no_conflict(self):

        file_name = "test_file.txt"

        source_file_path = self.source_dir / file_name
        source_file_path.write_text("This is a test file.")

        result = _handle_file_exists_at_dest(
            source_file_path, self.destination_dir, self.source_dir
        )
        assert result == file_name

    def test_file_exists_at_dest(self):

        file_name = "test_file.txt"
        source_file_path = self.source_dir / file_name
        source_file_path.write_text("This is a test file.")

        destination_path = self.destination_dir / file_name
        destination_path.write_text("Existing file content.")

        result = _handle_file_exists_at_dest(
            source_file_path, self.destination_dir, self.source_dir
        )
        assert result == "test_file (1).txt"

    def test_multiple_file_exists_at_dest(self):

        file_name = "test_file.txt"
        source_file_path = self.destination_dir / file_name
        source_file_path.write_text("This is a test file.")

        destination_path_numbered = self.destination_dir / "test_file (1).txt"
        destination_path_numbered.write_text("Another existing file.")

        result = _handle_file_exists_at_dest(
            source_file_path, self.destination_dir, self.source_dir
        )

        assert result == "test_file (2).txt"
