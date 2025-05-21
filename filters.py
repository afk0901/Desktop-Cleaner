import os
from sentry_sdk import add_breadcrumb


def filter_by_extensions(
    directory_content: list[str], extensions: list[str]
) -> list[str]:
    """
    Returns filtered files by given extensions.

    Args:
        directory_content: Content of a directory. Files and/or folders.
        extensions: Extensions that should be matched.
    """

    # Converting extensions to a set for O(1) lookup for the extensions list
    # as set is implemented as a hash table under the hood.
    # Using frozenset to make it immutable.
    extensions_set = frozenset(e.lower() for e in extensions)

    filtered = []

    for file in directory_content:
        _, extension = os.path.splitext(file)

        if extension.lower() in extensions_set:  # O(1)
            add_breadcrumb(
                category="Filtering operation",
                message=f"file {file} filtered by {extension.lower()}",
                level="info",
            )
            filtered.append(file)

    return filtered
