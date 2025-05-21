from pathlib import Path
import os
from move import move_multiple_files_by_dir_contents
from sentry_config import load_sentry_config
from sentry_sdk import add_breadcrumb
from win_reg_reader import get_windows_desktop_path
from filters import filter_by_extensions


def create_directory_by_filtered_directory_content(
    source_directory_path: Path,
    filtered_directory_content: list[str],
    new_directory_name: str,
) -> None:
    """
    creates a new directory if filtered_source_directory_content is not empty.
    Args:
        source_directory_path: Path of the source directory.
        new_directory_name: The name of the new directory inside the source directory.
    """

    if len(filtered_directory_content) > 0:
        Path(source_directory_path, new_directory_name).mkdir(exist_ok=True)


def _organize_directory_content_by_extensions(
    source_directory_path: Path,
    source_directory_content: list[str],
    dest_directory_name: str,
    extensions: list[str],
) -> None:
    """
    Creates a new directory in the source directory, moves the files according to the extensions
    list to the destination directory.
    Args:
        source_directory_path: Path of the source directory.
        new_directory_name: The name of the new directory inside the source directory.
        extensions: List of extensions to move to the folder.
    """
    add_breadcrumb(
        category="Prep",
        message=f"Preparing to move files with one of the extensions: {extensions}"
        f" from: {source_directory_path} into {dest_directory_name} at {source_directory_path}",
        level="info",
    )

    filtered_source_directory_content = filter_by_extensions(
        source_directory_content, extensions
    )

    create_directory_by_filtered_directory_content(
        source_directory_path, filtered_source_directory_content, dest_directory_name
    )

    move_multiple_files_by_dir_contents(
        source_directory_path, dest_directory_name, filtered_source_directory_content
    )


def _organize_files(source_directory_path: Path) -> None:
    """
    Organizes files in a source directory to subfolder in the same directory by extensions.
    Args:
        directory_path: The path of the directory to organize.
    """

    source_directory_content = os.listdir(source_directory_path)

    FILE_CATEGORIES = {
        "images": [".jpg", ".jpeg", ".png", ".webp", ".bmp"],
        "PDF Documents": [".pdf"],
        "Word Documents": [".doc", ".docx", ".odt"],
        "Excel Documents": [".csv", ".xlsx", ".ods"],
        "Text Documents": [".txt"],
    }

    add_breadcrumb(
        category="Prep",
        message=f"Preparing to move files from the file categories",
        level="info",
    )

    for category, extensions in FILE_CATEGORIES.items():

        _organize_directory_content_by_extensions(
            source_directory_path, source_directory_content, category, extensions
        )


def organize() -> None:
    """Organizes all the files by extensions"""
    path = get_windows_desktop_path()

    add_breadcrumb(
        category="Prep",
        message=f"Preparing to organize files at: {path}",
        level="info",
    )

    _organize_files(path)


def main() -> None:
    print("Cleaning your Desktop, please hold...")
    organize()
    print("Cleaning is complete. You may close the application.")


if __name__ == "__main__":
    load_sentry_config()
    main()
