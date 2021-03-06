from desktopmagic.screengrab_win32 import getDisplaysAsImages
from time import sleep
import datetime
import keyboard
import os
import json

ZOOM_ON_SCREEN = 1
CLASS_FOLDER = 'classes/'
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

def screenshot(end_time, interval, zoom_position=ZOOM_ON_SCREEN):
    SAVE_FOLDER = create_save_folder()
    interval = (interval * 60) - 2 # convert to seconds and account for two seconds delay every screenshots
    while (time := datetime.datetime.now()) < end_time:
        keyboard.send('alt+u')
        sleep(1)
        for displayNumber, im in enumerate(getDisplaysAsImages(), 1):
            if displayNumber == zoom_position:
                str_time = ''.join([ '.' if x == ':' else x for x in list(str(time))])
                filename = f'{SAVE_FOLDER}{str_time}.png'
                im.save(filename, format='png')
                print(filename)
        sleep(1)
        keyboard.send('alt+u')
        sleep(interval)