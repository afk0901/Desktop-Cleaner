import winreg
from sentry_sdk import capture_exception, add_breadcrumb


def _query_windows_desktop_path(key) -> str:
    reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key)
    desktop_path, type = winreg.QueryValueEx(reg, "Desktop")
    return desktop_path


def get_windows_desktop_path() -> str:
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
        desktop_path = _query_windows_desktop_path(key)
    except OSError as e:
        capture_exception(e)
        print(
            "Failed to read desktop path in the registry. Make sure you have the correct permissions and then try again."
        )
        return None

    except Exception as e:
        capture_exception(e)
        print("Failed to get the windows desktop path. Cause unknown.")
        return None
    return desktop_path
