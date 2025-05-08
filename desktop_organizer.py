from pathlib import Path
import os
from move import move_by_extension
from sentry_config import load_sentry_config
from sentry_sdk import add_breadcrumb
from win_reg_reader import get_windows_desktop_path
from filters import filter_by_extensions
import ctypes


def refresh_windows_desktop() -> None:
    """Refreshes the Desktop itself to temporarly prevent caching."""
    SHCNE_ASSOCCHANGED = 0x08000000
    SHCNF_IDLIST = 0x0000
    ctypes.windll.shell32.SHChangeNotify(SHCNE_ASSOCCHANGED, SHCNF_IDLIST, None, None)


def _organize_directory_content_by_extensions(
    source_directory_path: str,
    source_directory_content,
    new_directory_name: str,
    extensions: list[str],
) -> None:
    """
    Creates a new directory in the source directory, moves the files according to the extensions list to the new directory.
    Args:
        source_directory_path: Path of the source directory.
        new_directory_name: The name of the new directory inside the source directory.
        extensions: List of extensions to move to the folder.
    """
    filtered_source_directory_content = filter_by_extensions(
        source_directory_content, extensions
    )

    add_breadcrumb(
        category="Prep",
        message=f"Preparing to move files with one of the extensions: {extensions}"
        f" from: {source_directory_path} into {new_directory_name} at {source_directory_path}",
        level="info",
    )
    # Preventing creating empty folders.
    if len(filtered_source_directory_content) > 0:
        Path(source_directory_path, new_directory_name).mkdir(exist_ok=True)

    move_by_extension(
        source_directory_path, new_directory_name, filtered_source_directory_content
    )
    refresh_windows_desktop()


def _organize_files(source_directory_path: str) -> None:
    """
    Organizes files in a folder to subfolder by extensions.
    Args:
        directory_path: The path of the directory to organize.
    """

    source_directory_content = os.listdir(source_directory_path)

    _organize_directory_content_by_extensions(
        source_directory_path,
        source_directory_content,
        "images",
        [".jpg", "jpeg", ".png", ".webp", ".bmp"],
    )
    _organize_directory_content_by_extensions(
        source_directory_path, source_directory_content, "PDF Documents", [".pdf"]
    )
    _organize_directory_content_by_extensions(
        source_directory_path,
        source_directory_content,
        "Word Documents",
        [".doc", ".docx", ".odt"],
    )
    _organize_directory_content_by_extensions(
        source_directory_path,
        source_directory_content,
        "Excel files",
        [".csv", ".xlsx"],
    )
    _organize_directory_content_by_extensions(
        source_directory_path, source_directory_content, "Text files", [".txt"]
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


def main():
    print("Cleaning your Desktop, please hold...")
    organize()
    print("Cleaning is complete. You may close the application.")


if __name__ == "__main__":
    load_sentry_config()
    main()
