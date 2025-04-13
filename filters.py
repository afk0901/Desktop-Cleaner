import os
from sentry_sdk import add_breadcrumb


def filter_by_extensions(directory_content: list[str], extensions: list[str]):
    """
    Returns filtered files by given extensions.

    Args:
        directory_content: Content of a directory. Files and/or folders.
        extensions: Extensions that should be matched.
    """
    filtered = []

    for file in directory_content:
        _, extension = os.path.splitext(file)

        if extension.lower() in extensions:
            add_breadcrumb(
                category="Filtering operation",
                message=f"file {file} filtered by {extension.lower()}",
                level="info",
            )
            filtered.append(file)

    add_breadcrumb(
        category="Filtering operation",
        message=f"All files filtered. Extensions were {extensions}",
        level="info",
    )
    return filtered
