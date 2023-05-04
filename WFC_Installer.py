import subprocess
import converter

try:
    from context_menu import menus
except ImportError:
    subprocess.call("pip install -r requirements.txt", shell=True)
    from context_menu import menus


if __name__ == '__main__':
    try:
        menus.removeMenu('Convert to...', 'FILES')
    except FileNotFoundError:
        pass
    converter_menu = menus.ContextMenu('Convert to...', type='FILES')
    audio_menu = menus.ContextMenu('audio...', type='FILES')
    video_menu = menus.ContextMenu('video...', type='FILES')
    image_menu = menus.ContextMenu('image...', type='FILES')

    audio_menu.add_items([
        menus.ContextCommand(name="WAV", python=converter.convert, params='wav false'),
        menus.ContextCommand(name="MP3", python=converter.convert, params='mp3 false'),
        menus.ContextCommand(name="FLAC", python=converter.convert, params='flac false'),
        menus.ContextCommand(name="OGG", python=converter.convert, params='ogg false'),
        menus.ContextCommand(name="M4A", python=converter.convert, params='m4a false'),
        menus.ContextCommand(name="AAC", python=converter.convert, params='aac false'),
        menus.ContextCommand(name="WMA", python=converter.convert, params='wma false'),
        menus.ContextCommand(name="OPUS", python=converter.convert, params='opus false'),
        menus.ContextCommand(name="AC3", python=converter.convert, params='ac3 false'),
    ])

    video_menu.add_items([
        menus.ContextCommand(name="MP4", python=converter.convert, params='mp4 false'),
        menus.ContextCommand(name="AVI", python=converter.convert, params='avi false'),
        menus.ContextCommand(name="MKV", python=converter.convert, params='mkv false'),
        menus.ContextCommand(name="MOV", python=converter.convert, params='mov false'),
        menus.ContextCommand(name="FLV", python=converter.convert, params='flv false'),
        menus.ContextCommand(name="WMV", python=converter.convert, params='wmv false'),
        menus.ContextCommand(name="WEBM", python=converter.convert, params='webm false'),
        menus.ContextCommand(name="M4V", python=converter.convert, params='m4v false'),
    ])

    image_menu.add_items([
        menus.ContextCommand(name="PNG", python=converter.convert, params='png false'),
        menus.ContextCommand(name="JPG", python=converter.convert, params='jpg false'),
        menus.ContextCommand(name="GIF", python=converter.convert, params='gif false'),
        menus.ContextCommand(name="BMP", python=converter.convert, params='bmp false'),
        menus.ContextCommand(name="TIFF", python=converter.convert, params='tiff false'),
        menus.ContextCommand(name="WEBP", python=converter.convert, params='webp false'),
        menus.ContextCommand(name="ICO", python=converter.convert, params='ico false'),
    ])

    converter_menu.add_items([
        audio_menu,
        video_menu,
        image_menu,
    ])

    converter_menu.compile()
    print("[ WFC has been installed/updated. Do not move those files from this folder, or you cant uninstall/update WFC. ]")
    print("- If you want to uninstall WFC, run WFC_Uninstaller.py.")
    print("- If you want to update WFC, run WFC_Installer.py again.")
    print("- If you installed WFC in the wrong folder, run WFC_Uninstaller.py, change the folder, and run WFC_Installer.py again.")
    input("Press enter to continue...")

