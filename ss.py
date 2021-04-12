from desktopmagic.screengrab_win32 import getDisplaysAsImages
from time import sleep
import datetime
import os

ZOOM_ON_SCREEN = 2
CLASS_FOLDER = 'Classes/'
DELAY = 60 * 5
SAVE_FOLDER = ''

if not os.path.exists(CLASS_FOLDER):
    os.mkdir(CLASS_FOLDER)

def create_save_folder(folder=None):
    global CLASS_FOLDER
    if not folder:
        tm = datetime.datetime.now()
        folder = f'{CLASS_FOLDER}{tm.strftime("%c")}/'
        folder = ''.join([ '.' if x == ':' else x for x in list(str(folder)) ])
    os.mkdir(folder)
    return folder

def screenshot(end_time):
    SAVE_FOLDER = create_save_folder()
    while datetime.datetime.now() < end_time:
        for displayNumber, im in enumerate(getDisplaysAsImages(), 1):
            if displayNumber == ZOOM_ON_SCREEN:
                time = datetime.datetime.now()
                str_time = ''.join([ '.' if x == ':' else x for x in list(str(time))])
                filename = f'{SAVE_FOLDER}{str_time}.png'
                im.save(filename, format='png')
                print(filename)
        sleep(DELAY)