from pathlib import Path
import os
from move import move_by_extension
from sentry_config import load_sentry_config
from sentry_sdk import add_breadcrumb
from win_reg_reader import get_windows_desktop_path


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
    add_breadcrumb(
        category="Prep",
        message=f"Preparing to move files with one of the extensions: {extensions}"
        f" from: {source_directory_path} into {new_directory_name} at {source_directory_path}",
        level="info",
    )

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
    _organize_directory_content_by_extensions(directory_path, "PDF Documents", [".pdf"])
    _organize_directory_content_by_extensions(
        directory_path, "Word Documents", [".doc", ".docx"]
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
