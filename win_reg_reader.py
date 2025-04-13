import winreg
from sentry_sdk import capture_exception, add_breadcrumb


def _read_windows_registry(key: str) -> str | None:
    """Opening HKEY_CURRENT_USER registry key returning a winreg object.
    Args:
        key: Key to the Windows registry
    """
    try:
        add_breadcrumb(
            category="Registry",
            message="Opening HKEY_CURRENT_USER registry key",
            level="info",
        )
        return winreg.OpenKey(winreg.HKEY_CURRENT_USER, key)
    except Exception as e:
        capture_exception(e)
        print("Failed to read registry:", e)


def get_windows_desktop_path() -> str:
    """
    Gets the path for the Desktop from the registry.
    As for Windows, the Desktop path is not always the same, for example if OneDrive
    is used. Therefore, registry is used instead.
    """
    # What's a registry and how does it work?
    key = r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
    reg = _read_windows_registry(key)
    desktop_path, _ = winreg.QueryValueEx(reg, "Desktop")
    return desktop_path
