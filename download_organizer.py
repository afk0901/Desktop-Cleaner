from pathlib import Path
import os
import logging
from move import move_by_extension

# TODO: Add logging, error handling, edge cases.
# TODO: When file downloads, automatically organize the files.


def _organize_directory_content_by_extensions(
    source_directory_path: str, new_directory_name: str, extensions: list[str]
) -> None:
    """
    Creates a new directory in the source directory, moves the files according to the extensions list to the new directory.
    Args:
        source_directory_path: Path of the source directory.
        new_directory_name: The name of the new directory inside the source directory.
        extensions: List of extensions to move to the folder.
    """
    Path(source_directory_path, new_directory_name).mkdir(exist_ok=True)
    directory_content = os.listdir(source_directory_path)
    move_by_extension(
        source_directory_path, new_directory_name, extensions, directory_content
    )


def _organize_files(directory_path: str) -> None:
    """
    Organizes files in a folder to subfolder by extensions.
    Args:
        directory_path: The path of the directory to organize.
    """
    _organize_directory_content_by_extensions(
        directory_path, "images", [".jpg", "jpeg", ".png", ".webp", ".bmp"]
    )
    _organize_directory_content_by_extensions(directory_path, "pdf documents", [".pdf"])
    _organize_directory_content_by_extensions(
        directory_path, "Word documents", [".doc", ".docx"]
    )


def main():
    downloads_path = Path.home() / "Downloads"
    _organize_files(downloads_path)


if __name__ == "__main__":
    main()
