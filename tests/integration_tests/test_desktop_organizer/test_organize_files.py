from desktop_organizer import _organize_files
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

    def list_new_dir_content(self, new_dir_name: str) -> list[str]:
        """
        Helper function to list the content of a new directory.
        Args:
            new_dir_name: The name of the new directory. 

        """
        new_dir = Path(self.source_directory_path) / Path(new_dir_name)
        return os.listdir(new_dir)

    def test_organize_images_in_images_folder(self):
        _organize_files(self.source_directory_path)
        new_dir_content = self.list_new_dir_content("images")
        
        assert new_dir_content.sort() == [
            "test_file1.jpg",
            "test_file2.png",
            "test_file5.jpeg",
            "test_file6.webp",
            "test_file7.bmp",
        ].sort()

    def test_organize_word_docs_in_word_docs_folder(self):
        _organize_files(self.source_directory_path)
        new_dir_content = self.list_new_dir_content("Word Documents")
        
        assert new_dir_content.sort() == [
            "test_file3.docx",
            "test_file4.doc",
        ].sort()

    def test_organize_excel_files_in_excel_files_folder(self):
        _organize_files(self.source_directory_path)
        new_dir_content = self.list_new_dir_content("Excel files")
        
        assert new_dir_content.sort() == [
            "test_file8.csv",
            "test_file9.xlsx",
        ].sort()

    def test_organize_pdf_files_in_pdf_files_folder(self):
        _organize_files(self.source_directory_path)
        new_dir_content = self.list_new_dir_content("PDF Documents")
        
        assert new_dir_content.sort() == [
            "test_file10.pdf",
        ].sort()

    def test_organize_text_files_in_text_files_folder(self):
        _organize_files(self.source_directory_path)
        new_dir_content = self.list_new_dir_content("Text files")
        
        assert new_dir_content.sort() == [
            "test_file11.txt",
        ].sort()
        