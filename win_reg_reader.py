import winreg
from sentry_sdk import capture_exception, add_breadcrumb


def get_windows_desktop_path() -> str:
    """
    Gets the path for the Desktop from the registry.
    As for Windows, the Desktop path is not always the same, for example if OneDrive
    is used. Therefore, registry is used instead.
    """
    # What's a registry and how does it work?
    key = r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
    add_breadcrumb(
        category="Registry",
        message="Referencing and reading desktop path from registry",
        level="info",
    )
    try:
        reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key)
        desktop_path, type = winreg.QueryValueEx(reg, "Desktop")
    except OSError as e:
        capture_exception(e)
        print(
            "Failed to read desktop path in the registry. Make sure you have the correct permissions and then try again."
        )

    except Exception as e:
        capture_exception(e)
        print("Failed to get the windows desktop path. Cause unknown.")
    return desktop_path
