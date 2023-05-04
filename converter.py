import subprocess


def convert(file, params):
    file = file[0]
    params = params.split(' ')
    ext = params[0]
    debug = params[1] == 'true'
    # debug = True  # Remove the comment from this line to enable debug mode
    # TODO: replace the debug variable with a function that runs debug mode if the user holds shift while clicking the menu item
    print(file, debug)
    subprocess.call('ffmpeg -i "{}" "{}"'.format(file, file.replace(file.split('.')[-1], ext)), shell=True)
    if debug: input("Press enter to continue...")


if __name__ == '__main__':
    print("This file is not meant to be run directly. Please run WFC_Installer.py instead. Right click on any audio/picture file to see the new 'Convert to...' context menu.")
    input("Press enter to continue...")
