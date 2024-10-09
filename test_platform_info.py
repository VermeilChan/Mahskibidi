import platform

def get_linux_platform_info():
    try:
        os_info = platform.freedesktop_os_release()

        os_name = os_info.get("NAME", "N/A")
        os_id = os_info.get("ID", "N/A")
        pretty_name = os_info.get("PRETTY_NAME", "N/A")
        version_id = os_info.get("VERSION_ID", "N/A")
        id_like = os_info.get("ID_LIKE", "N/A")

        print("=== Linux Platform Information ===")
        print(f"OS Name: {os_name}")
        print(f"OS ID: {os_id}")
        print(f"Pretty Name: {pretty_name}")
        print(f"Version ID: {version_id}")
        print(f"ID_Like: {id_like}")
        print("==================================")

    except OSError as e:
        print(f"Error reading os-release file: {e}")

def get_windows_platform_info():
    win32_ver = platform.win32_ver()
    release, version, csd, ptype = win32_ver

    edition = platform.win32_edition()
    is_iot = platform.win32_is_iot()

    print("=== Windows Platform Information ===")
    print(f"OS Release: {release if release else 'N/A'}")
    print(f"OS Version: {version if version else 'N/A'}")
    print(f"CSD Level: {csd if csd else 'N/A'}")
    print(f"OS Type: {ptype if ptype else 'N/A'}")
    print(f"Windows Edition: {edition if edition else 'N/A'}")
    print(f"Is IoT Edition: {'Yes' if is_iot else 'No'}")
    print("====================================")

def get_mac_platform_info():
    system = platform.system()
    release = platform.release()
    version = platform.version()

    print("=== macOS Platform Information ===")
    print(f"System: {system}")
    print(f"Release: {release}")
    print(f"Version: {version}")
    print("==================================")

if __name__ == "__main__":
    if platform.system() == "Linux":
        get_linux_platform_info()
    elif platform.system() == "Windows":
        get_windows_platform_info()
    elif platform.system() == "Darwin":
        get_mac_platform_info()
