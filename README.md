# WinFileConverter
A file converter, using the native context menu. Convert audio, video and image files easily by right-clicking it.

![alt text](/rm/wfc.png)
## How to install WFC
- Move the repository into any folder, which you won't touch at any time (Documents Folder, User Folder etc.)
- Run ``WFC_Installer.py``
- WFC is now successfully installed

## How to update WFC
- Download the new ``WFC_Installer.py``
- Run ``WFC_Installer.py``
- WFC is now successfully updated (it replaced the old WFC)

## How to uninstall WFC
- Run ``WFC_Uninstall.py``
- WFC should now be uninstalled. If not, open issues.

## Debug mode
- Open ``converter.py``
- Remove the comment in ``line 9`` to overwrite the Debug mode
- Debug mode on true just lets the terminal stay opened.

## Problems...
### WFC is still installed/can't uninstall
- Make sure, that you haven't changed the directory. This program is limited by using absolute paths.
### Some options to convert files are missing
- It's also a limitation, this time by Windows. Context-menus can only have 16 Items.
