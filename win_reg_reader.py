import winreg
from sentry_sdk import capture_exception, add_breadcrumb
from pathlib import Path
from error_handling import error_message_prompt_and_exit

def _query_windows_registry(key: str, name: str) -> Path:
    """
    Queries the Windows registry by a string indicating the value to query.

    Args:
        key: A string indicating the registry key to query.
        name: A string indicating the value to query.

    Returns: The value of the registry key by the name.
    """
    reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key)
    desktop_path, type = winreg.QueryValueEx(reg, name)
    return Path(desktop_path)


def get_windows_desktop_path() -> Path:
    """
    Gets the path for the Desktop from the registry.
    As for Windows, the Desktop path is not always the same, for example if OneDrive
    is used. Therefore, registry is used instead.
    """

    key = r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"

    add_breadcrumb(
        category="Registry",
        message="Referencing and reading desktop path from registry",
        level="info",
    )
    try:
        desktop_path = _query_windows_registry(key, "Desktop")
        return desktop_path
    except OSError as e:
        capture_exception(e)
        error_msg = "Failed to read desktop path in the registry. Make sure you have the correct permissions and then try again."
        error_message_prompt_and_exit(error_msg)
    except Exception as e:
        capture_exception(e)
        error_msg = "Failed to get the windows desktop path. Cause unknown."
        error_message_prompt_and_exit(error_msg)
