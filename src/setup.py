import subprocess
import sys
import os

SRC_PATH = 'src'
WEBDRIVER_PATH = 'webdriver'

subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", os.path.join(SRC_PATH, "requirements.txt")])

from selenium import webdriver
from time import sleep
import stdiomask
import mouse
import keyboard
import json

URL = 'https://binus.zoom.us/j/00000000000?pwd=000000000000'
CONFIG_FILE_PATH = os.path.join(SRC_PATH, 'config.json')
DEFAULT_CONFIG_DATA = {
    'binumaya_username' : '',
    'binusmaya_password' : '',
    'zoom_position' : '1',
    'browser' : 'chrome',
    'time_offset' : 0,
    'zoom_launch_button_x' : '0',
    'zoom_launch_button_y' : '0',
    'zoom_open_button_x' : '0',
    'zoom_open_button_y' : '0',
    'screenshot_interval': 0
}
CONFIG_DATA = {}
BROWSER_TYPES = ('chrome', 'firefox', 'edge')
TIME_ZONES = (0, 1, 2)
HEADER = '''
░██████╗███████╗████████╗██╗░░░██╗██████╗░
██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗
╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝
░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░
██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░
╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░
           Created by deXOR0
'''

def error(msg):
    print(f'[ERROR] - {msg}')

def init():
    print(HEADER)
    print()
    print('Loading config...')
    if not os.path.isfile(CONFIG_FILE_PATH):
        print('Config is not found, performing first time setup...')
        with open(CONFIG_FILE_PATH, 'w') as file:
            file.write(json.dumps(DEFAULT_CONFIG_DATA))

    with open(CONFIG_FILE_PATH, 'r') as file:
        CONFIG_DATA = json.loads(file.read())
    
    print('Config loaded')

if __name__ == '__main__':
    init()

    CONFIG_DATA['binusmaya_username'] = input('Input your Binusmaya username (without @binus.ac.id): ')
    CONFIG_DATA['binusmaya_password'] = stdiomask.getpass(prompt='Input your Binusmaya password: ', mask='•')

    print()

    multiple_monitor = 'n'
    while True:

        multiple_monitor = input('Do you use more than 1 monitor in your setup? (y/n): ').lower()

        if multiple_monitor == 'y' or multiple_monitor == 'n':
            break

    CONFIG_DATA['zoom_position'] = 1
    if multiple_monitor == 'y':
        while True:

            try:
                CONFIG_DATA['zoom_position'] = int(input('Which monitor do you use for zoom meeting? (1-n): '))
            except:
                error('Input must be a number!')

            if CONFIG_DATA['zoom_position'] >= 1:
                break
    browser = -1

    print()

    while True:

        print('Browser Type')
        print('====================')
        print('1. Google Chrome')
        print('2. Mozilla Firefox')
        print('3. Microsoft Edge')
        try:
            browser = int(input('> '))
        except:
            error('Input must be a number!')

        if browser >= 1 or browser <= 3:
            break

    CONFIG_DATA['browser'] = BROWSER_TYPES[browser-1]

    print()

    interval = -1

    while True:

        print('For documentation purposes, AutoZoom will take screenshots every few minutes')
        print("Set the interval between each screenshots (0 if you don't want to take any)")
        try:
            interval = int(input('> '))
        except:
            error('Input must be a whole number!')

        if browser >= 0:
            break

    CONFIG_DATA['screenshot_interval'] = interval

    print()

    while True:

        print('Select your time zone')
        print('======================')
        print('1. UTC+7 (WIB)')
        print('2. UTC+8 (WITA)')
        print('3. UTC+9 (WIT)')
        print('4. Other')
        try:
            time_zone = int(input('> '))
        except:
            error('Input must be a number!')

        if time_zone == 4:
            while True:
                try:
                    CONFIG_DATA['time_offset'] = int(input('\nTime offset relative to UTC+7 in hours (Ex: UTC+6 = -1): '))
                    break
                except:
                    error('Input must be a number!')
            break
        elif time_zone >= 1 or time_zone <= 3:
            CONFIG_DATA['time_offset'] = TIME_ZONES[time_zone-1]
            break
    
    driver=None
    if CONFIG_DATA['browser'] == 'chrome':
        driver = webdriver.Chrome(os.path.join(WEBDRIVER_PATH, 'chromedriver.exe'))
    elif CONFIG_DATA['browser'] == 'firefox':
        driver = webdriver.Firefox(os.path.join(WEBDRIVER_PATH, 'geckodriver.exe'))
    elif CONFIG_DATA['browser'] == 'edge':
        driver = webdriver.Edge(os.path.join(WEBDRIVER_PATH, 'MicrosoftWebDriver.exe'))

    print()

    driver.get(URL)
    print('Wait for the browser to open zoom launch meeting page')
    # Firefox specific command
    if CONFIG_DATA['browser'] == 'firefox':
        sleep(5)
        keyboard.send('enter')
        sleep(5)
    confirm = 'n'
    while confirm == 'n':
        print("Record 'Launch Meeting' button")
        confirm = input('Are you ready?\n(y/n)> ').lower()
        if confirm == 'y':
            print("Hover your cursor on 'Launch Meeting' button")
            n = 5
            while n >= 0:
                print(f'Recording in {n} seconds...')
                n -= 1
                sleep(1)
            CONFIG_DATA['zoom_launch_button_x'], CONFIG_DATA['zoom_launch_button_y'] = mouse.get_position()
            print(f"({CONFIG_DATA['zoom_launch_button_x']}, {CONFIG_DATA['zoom_launch_button_y']})")
            confirm = input('Is this correct?\n(y/n)> ').lower()
            if confirm == 'y':
                break
        elif confirm == 'n':
            continue
        else:
            error('Input must be y or n!')
            confirm = 'n'
    
    print()

    if CONFIG_DATA['browser'] == 'firefox':
        confirm = 'n'
        while confirm == 'n':
            print("Record 'Choose Application' button")
            confirm = input('Are you ready?\n(y/n)> ').lower()
            if confirm == 'y':
                print("Hover your cursor on 'Launch Meeting' button")
                n = 5
                while n >= 0:
                    print(f'Recording in {n} seconds...')
                    n -= 1
                    sleep(1)
                CONFIG_DATA['firefox_choose_application_button_x'], CONFIG_DATA['firefox_choose_application_button_y'] = mouse.get_position()
                print(f"({CONFIG_DATA['firefox_choose_application_button_x']}, {CONFIG_DATA['firefox_choose_application_button_y']})")
                confirm = input('Is this correct?\n(y/n)> ').lower()
                if confirm == 'y':
                    break
            elif confirm == 'n':
                continue
            else:
                error('Input must be y or n!')
                confirm = 'n'
        
        print()

    confirm = 'n'
    while confirm == 'n':
        print("Record 'Open Zoom Meetings' button")
        confirm = input('Are you ready?\n(y/n)> ').lower()
        if confirm == 'y':
            print("Hover your cursor on 'Open Zoom Meetings' button")
            n = 5
            while n >= 0:
                print(f'Recording in {n} seconds...')
                n -= 1
                sleep(1)
            CONFIG_DATA['zoom_open_button_x'], CONFIG_DATA['zoom_open_button_y'] = mouse.get_position()
            print(f"({CONFIG_DATA['zoom_open_button_x']}, {CONFIG_DATA['zoom_open_button_y']})")
            confirm = input('Is this correct?\n(y/n)> ').lower()
            if confirm == 'y':
                break
        elif confirm == 'n':
            continue
        else:
            error('Input must be y or n!')
            confirm = 'n'
    
    with open(CONFIG_FILE_PATH, 'w') as file:
        print('Saving config...')
        file.truncate(0)
        file.write(json.dumps(CONFIG_DATA))
    
    print('Config saved! You can use the application now!')
