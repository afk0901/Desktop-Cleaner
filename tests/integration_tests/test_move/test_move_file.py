import pytest
from move import _move_file
from tests.move_set_up_tear_down import setUpTearDown
from pathlib import Path


class TestMoveFile:

    def setup_method(self):
        self.setup_teardown = setUpTearDown()
        self.setup_teardown.setup()
        self.source_dir = self.setup_teardown.get_source_dir_path()
        self.destination_dir = self.setup_teardown.get_destination_dir_path()

    def teardown_method(self):
        self.setup_teardown = setUpTearDown()
        self.setup_teardown.teardown()

    def test_move_file_success(self):
        file_path = self.source_dir / "test_file.txt"
        file_path.write_text("This is a test file.")

        _move_file(self.source_dir, self.destination_dir.name, file_path.name)

        moved_file_path = self.destination_dir / "test_file.txt"
        moved_file_path = self.destination_dir / "test_file.txt"
        assert moved_file_path.exists()
        assert not file_path.exists()
        assert moved_file_path.read_text() == "This is a test file."

    def test_move_file_nonexistent_source(self):
        file_path = self.source_dir / "nonexistent_file.txt"

        with pytest.raises(FileNotFoundError):
            _move_file(self.source_dir, self.destination_dir.name, file_path.name)


class TestFileExistsAtDestinationWithMoveFile:

    def setup_method(self):
        self.setup_teardown = setUpTearDown()
        self.setup_teardown.setup()
        self.source_dir = self.setup_teardown.get_source_dir_path()
        self.destination_dir = self.setup_teardown.get_destination_dir_path()

    def teardown_method(self):
        self.setup_teardown = setUpTearDown()
        self.setup_teardown.teardown()

    def test_move_file_destination_exists(self):

        file_path = self.source_dir / "test_file.txt"
        file_path.write_text("This is a test file.")

        file_path_dest = self.destination_dir / "test_file.txt"
        file_path_dest.write_text("This is a test file.")

        _move_file(self.source_dir, self.destination_dir.name, file_path.name)

        new_file_path = self.destination_dir / "test_file (1).txt"
        assert new_file_path.exists()
        assert not file_path.exists()
        assert new_file_path.read_text() == "This is a test file."

    def test_move_file_multiple_existing_files(self):

        source_file_path = Path(self.source_dir) / Path("test_file.txt")
        source_file_path.write_text("This is a test file.")

        dest_file_path = Path(self.destination_dir) / Path("test_file.txt")
        dest_file_path.write_text("Existing file content.")

        dest_file_path_numbered = Path(self.destination_dir) / Path("test_file (1).txt")
        dest_file_path_numbered.write_text("Another existing file.")

        _move_file(self.source_dir, self.destination_dir.name, source_file_path.name)

        new_file_path = self.destination_dir / "test_file (2).txt"
        assert new_file_path.exists()
        assert not source_file_path.exists()
        assert new_file_path.read_text() == "This is a test file."
