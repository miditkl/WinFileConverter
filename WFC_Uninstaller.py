import subprocess

try:
    from context_menu import menus
except ImportError:
    subprocess.call("pip install -r requirements.txt", shell=True)
    from context_menu import menus


if __name__ == '__main__':
    try:
        menus.removeMenu('Convert to...', 'FILES')
        print("WFC has been uninstalled.")
    except FileNotFoundError:
        print("WFC is not installed. Nothing to uninstall.")
