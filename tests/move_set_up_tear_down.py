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

    def setup(self):
        Path(self.get_test_dir_path()).mkdir(exist_ok=True)
        Path(self.get_destination_dir_path()).mkdir(exist_ok=True)

    def teardown(self):
        shutil.rmtree(self.get_test_dir_path())
