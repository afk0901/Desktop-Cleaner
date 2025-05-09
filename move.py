import shutil
from pathlib import Path
import os
import re
from sentry_sdk import capture_exception
from sentry_sdk import add_breadcrumb


def _handle_file_exists_at_dest(
    source_file_path: Path, dest_dir_path: Path, source_file_name: str, source_dir_path
) -> str:
    """
    Handles the situation when a file already exists at the destination.
    Adds a (<some_number>) behind the file if the file already exists at the destination.
    Args:
        source_file_path: Full path of the source file
        dest_dir_path: Full path to the destination directory
        source_file_name: Source filename such as file.extension
        source_dir_path: Full path to the source directory
    """

    dest_file_path = Path(dest_dir_path) / Path(source_file_name)

    if os.path.exists(dest_file_path):

        add_breadcrumb(
            category="path operation",
            message=f"Handling path for moving {source_file_path} to {dest_dir_path} from {source_dir_path} when the path is the same.",
            level="info",
        )

        _, extension = os.path.splitext(Path(source_file_name))

        num = 0
        new_source_file_path = source_file_path.stem
        source_file_name = source_file_path.stem
        new_source_file = source_file_path.stem

        # If the destination file already exists, add a (number) behind it.
        while os.path.exists(dest_file_path):

            num += 1

            # Removes zero or more whitepaces including tabs, and ending with a digit inside if it's there.
            new_source_file = re.sub(r"\s*\(\d+\)$", "", source_file_name)
            new_source_file_path = Path(
                f"{source_dir_path}/{new_source_file} ({num}){extension}"
            )
            dest_file_path = Path(dest_dir_path) / Path(
                os.path.basename(new_source_file_path)
            )

        os.rename(source_file_path, new_source_file_path)

        add_breadcrumb(
            category="path operation",
            message=f" {dest_file_path} is safe to move.",
            level="info",
        )
    return os.path.basename(dest_file_path)


def _move_file(source_dir_path: str, dest_dir_name: str, file_name: str) -> None:
    """Performs the move itself, checks if file exists it renames the file being moved"""

    add_breadcrumb(
        category="moving operation",
        message=f"Moving the file {file_name}",
        level="info",
    )

    source_file_path = Path(source_dir_path) / Path(file_name)
    dest_dir_path = Path(source_dir_path) / Path(dest_dir_name)

    source_file_path = Path(source_dir_path) / _handle_file_exists_at_dest(
        source_file_path, dest_dir_path, file_name, source_dir_path
    )

    shutil.move(source_file_path, dest_dir_path)


def _safe_move(source_directory_path: str, dest_directory_name: str, file: str) -> None:
    """Moves a file inside the source directory to another directory and handles edge cases.
    If the source file is read-only a message is printed.
    Catches any other exception and prints an appropriate message.
    Args:
     source_directory_path: The path of the source directory.
     dest_directory_name: New directory name that will be stored in the source directory.
     file: The file to be moved.
    """

    try:
        _move_file(source_directory_path, dest_directory_name, file)
    except PermissionError as e:
        capture_exception(e)
        print(
            f"Permission denied for: {file}. Please check if the file is in use by another program or contact your administrator."
        )

    except Exception as e:
        capture_exception(e)
        print(f"Unexpected error while moving {file}: {e}")


def move_multiple_folder_contents(
    source_directory_path: str,
    new_directory_name: str,
    directory_content: list[str],
) -> None:
    """
    Moves files from the source directory to a new directory inside the source directory.
    Args:
        source_directory_path: The path of the source directory.
        new_directory_name: New directory name that will be stored in the source directory.
        directory_content: The content of the source directory, files and folders.
    """
    for file in directory_content:
        add_breadcrumb(
            category="moving operation",
            message=f"Performing move operation with _safe move for the file {file}",
            level="info",
        )
        _safe_move(source_directory_path, new_directory_name, file)
