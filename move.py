import shutil
from pathlib import Path
import os
import re

# TODO: Add logging

def _handle_file_exists_at_dest(source_file_path: Path, dest_dir_path: Path, source_file_name: str, source_dir_path):
    """
    Handles the situation when a file already exists at the destination. 
    Adds a (<some_number>) behind the file if the file already exists at the destination.
        Args:
        source_file_path: Full path of the source file
        dest_dir_path: Full path to the destination directory
        source_file_name: Source filename such as file.extension.
        source_dir_path: Full path to the source directory.
    """
    
    #TODO: Rename the file moved with a number attached to it,
    #like: file_1, file_2, file_y_1, file_y_2 and so on.
    # dest_file_name - the file name at the destination 

       #TODO: Clean me and keep testing edge cases, the (number) thing is good to go, if no more bugs 
       #are found. TODO: clean up the code a bit.

    dest_file_path = Path(dest_dir_path) / Path(source_file_name)
    if os.path.exists(dest_file_path):
        _, extension = os.path.splitext(Path(source_file_name))
        
        # In the case the destination file ends with the same number.
        num = 0
        new_source_file_path = source_file_path.stem
        source_file_name = source_file_path.stem
        new_source_file = source_file_path.stem
        while os.path.exists(dest_file_path):
            num += 1
            # If source file ends with (anynumbe) already, treat it as one without it. 
            if re.search(r"\(\d+\)$", source_file_name):
                new_source_file = f"{new_source_file[:-3].strip()} ({num})"
            else:
                new_source_file = f"{source_file_name} ({num})"
            new_source_file_path = Path(f"{source_dir_path}/{new_source_file}{extension}")
            # 1 doesnt exist anymore cuz it's renamed.
            os.rename(source_file_path, new_source_file_path)
            source_file_path = new_source_file_path
            dest_file_path = Path(dest_dir_path) / Path(os.path.basename(new_source_file_path))
    return os.path.basename(dest_file_path)

def _move_file(source_dir_path: str, dest_dir_name: str, file_name: str):
    """Performs the move itself, checks if file exists it renames the file being moved"""
    source_file_path = Path(source_dir_path) / Path(file_name)
    dest_dir_path = Path(source_dir_path) / Path(dest_dir_name)

    source_file_path = Path(source_dir_path) / _handle_file_exists_at_dest(source_file_path, dest_dir_path, file_name, source_dir_path)

    shutil.move(source_file_path, dest_dir_path)

def _safe_move(source_directory_path: str, dest_directory_name: str, file: str) -> None:
    """Moves a file inside the source directory to another directory and handles edge cases.
       1. If file exists, it renames the file.
       2. If the source file is read-only a message is printed.
    """
    try:
        _move_file(source_directory_path, dest_directory_name, file)
    except PermissionError:
        print(
            f"Permission denied for: {file}. Please check if the file is in use by another program or contact your administrator."
        )
    
    except Exception as e:
        print(f"Unexpected error while moving {file}: {type(e)}")


def move_by_extension(
    source_directory_path: str,
    new_directory_name: str,
    extensions: list[str],
    directory_content: list[str],
) -> None:
    """
    Checks if the extension is in the extensions list - if so, moves the files in the new directory.
    Args:
        source_directory_path: The path of the source directory.
        new_directory_name: New directory name that will be stored in the source directory.
        extensions: List of extensions to categorize such as .png, .jpeg, .jpg and so on for images.
        directory_content: The content of the source directory, files and folders.
    """
    for file in directory_content:
        _, extension = os.path.splitext(file)
        if extension.lower() in extensions:
            _safe_move(source_directory_path, new_directory_name, file)
