import requests
import json
import datetime
import time
import mouse
import keyboard
import ss
import os
from inputimeout import inputimeout, TimeoutOccurred
from selenium import webdriver

BASE = 'https://myclass.apps.binus.ac.id'
TODAY = datetime.datetime.now().strftime('%c').split(' ')
TODAY_CLASS_LIST = []
CONFIG_FILE_PATH = 'config.json'
CONFIG_DATA = {}
CUSTOM_JSON_FILE_PATH = 'custom.json'
CUSTOM_JSON_FILE_DEFAULT_DATA = [{
    'CourseTitleEn' : '',
    'DisplayStartDate' : '',
    'StartTime': '',
    'EndTime' : '',
    'MeetingUrl' : ''
}]
HEADER = '''

░█████╗░██╗░░░██╗████████╗░█████╗░  ███████╗░█████╗░░█████╗░███╗░░░███╗
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗  ╚════██║██╔══██╗██╔══██╗████╗░████║
███████║██║░░░██║░░░██║░░░██║░░██║  ░░███╔═╝██║░░██║██║░░██║██╔████╔██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║  ██╔══╝░░██║░░██║██║░░██║██║╚██╔╝██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝  ███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░  ╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝
                        Created by deXOR0
'''

def error(msg):
    print(f'[ERROR] - {msg}')

def init():
    global CONFIG_DATA, CONFIG_FILE_PATH
    print(HEADER)
    print()
    if not os.path.isfile(CONFIG_FILE_PATH):
        error('Config file not found!\nRun setup.py first!')
        quit()
    else:
        print('Loading config...')
        with open(CONFIG_FILE_PATH) as file:
            CONFIG_DATA = json.loads(file.read())
        print('Config loaded!')
    
    while True:
        print('Select an option')
        print('You have 5 seconds to select an option, otherwise, option 1 will be selected')
        print('1. Load Class data from MyClass API')
        print('2. Load data from json file')
        try:
            option = int(inputimeout(prompt='> ', timeout=5))
        except TimeoutOccurred:
            option = 1
        except:
            error('Input must be a number!')
        
        if option >= 1 and option <= 2:
            break
    
    if option == 1:
        get_class_from_api()
    elif option == 2:
        get_class_from_json()

def is_today(class_date):
    '''
    Returns true if the class date is the current date
    '''
    global TODAY
    TODAY = list(filter(None, TODAY))
    date, month, year = class_date.split(' ')
    date = str(int(date))
    # print(TODAY, date, month, year)
    
    return date == TODAY[2] and month == TODAY[1] and year == TODAY[4]

def zoom_class(zoom_link):
    '''
    Returns true if the class have a zoom link
    '''
    return zoom_link != '-'

def unique_class(start_time):
    '''
    Return true if the class start time does not conflict with another class
    '''
    if len(TODAY_CLASS_LIST) == 0:
        return True
    for _class in TODAY_CLASS_LIST:
        if start_time == _class['StartTime']:
            return False
    return True

def not_passed(end_time):
    '''
    Return true if current time  is less than or equal to class end time
    '''
    return datetime.datetime.now() <= build_datetime(end_time, hour_offset=CONFIG_DATA['time_offset'])

def build_datetime(time_string, hour_offset=0, minute_offset=0):
    '''
    Build Datetime object set to given time_string with a specified offset if provided
    '''
    time_list = [ int(x) for x in time_string.split(':') ]
    tm = datetime.datetime.now().replace(hour=(time_list[0] + hour_offset) % 24, minute=(time_list[1] + minute_offset) % 60, second=0, microsecond=0)
    return tm

def get_class_from_api():
    '''
    Get class data from myclass' api
    '''
    global TODAY_CLASS_LIST
    print('Getting class data from MyClass API...')
    payload = {'Username': CONFIG_DATA['binusmaya_username'], 'Password': CONFIG_DATA['binusmaya_password']}
    session = requests.Session()
    req = requests.Request('POST', f'{BASE}/Auth/Login', data=payload)
    p_req = session.prepare_request(req)

    response = session.send(p_req)

    schedule = session.get(f"{BASE}/Home/GetViconSchedule")

    lst = json.loads(schedule.text)

    # print(lst)

    for _class in lst:
        if is_today(_class['DisplayStartDate']) and zoom_class(_class['MeetingUrl']) and unique_class(_class['StartTime']) and not_passed(_class['EndTime']):
            new_class = {}
            new_class['CourseTitleEn'] = _class['CourseTitleEn']
            new_class['DisplayStartDate'] = _class['DisplayStartDate']
            new_class['StartTime'] = _class['StartTime']
            new_class['EndTime'] = _class['EndTime']
            new_class['MeetingUrl'] = _class['MeetingUrl']
            TODAY_CLASS_LIST.append(new_class)

def get_class_from_json():
    '''
    Get class data from json file
    '''
    global TODAY_CLASS_LIST, CUSTOM_JSON_FILE_PATH, CUSTOM_JSON_FILE_DEFAULT_DATA
    print(f'Getting class data from {CUSTOM_JSON_FILE_PATH}')
    if not os.path.exists(CUSTOM_JSON_FILE_PATH):
        print('File not found, generating file...')
        with open(CUSTOM_JSON_FILE_PATH, 'w') as file:
            file.write(json.dumps(CUSTOM_JSON_FILE_DEFAULT_DATA))
        print(f'{CUSTOM_JSON_FILE_PATH} generated, please edit with text editor!')
    else:
        with open(CUSTOM_JSON_FILE_PATH) as file:
            file_data = json.loads(file.read())
            for _class in file_data:
                if is_today(_class['DisplayStartDate']) and zoom_class(_class['MeetingUrl']) and unique_class(_class['StartTime']) and not_passed(_class['EndTime']):
                    new_class = {}
                    new_class['CourseTitleEn'] = _class['CourseTitleEn']
                    new_class['DisplayStartDate'] = _class['DisplayStartDate']
                    new_class['StartTime'] = _class['StartTime']
                    new_class['EndTime'] = _class['EndTime']
                    new_class['MeetingUrl'] = _class['MeetingUrl']
                    TODAY_CLASS_LIST.append(new_class)

if __name__ == '__main__':
    init()

    print(TODAY_CLASS_LIST)

    while len(TODAY_CLASS_LIST) > 0:
        next_class = TODAY_CLASS_LIST[0]
        next_class_start_time = build_datetime(next_class['StartTime'], hour_offset=CONFIG_DATA['time_offset'], minute_offset=-15)
        next_class_end_time = build_datetime(next_class['EndTime'], hour_offset=CONFIG_DATA['time_offset'])

        while (now := datetime.datetime.now()) < next_class_start_time:
            print(f"Next Class: {next_class['CourseTitleEn']}, Time: {next_class['StartTime']}, Now: {now}")
            time.sleep(1)
        
        keyboard.send('alt+q')
        print(f"Joining {next_class['CourseTitleEn']}")

        driver=None
        if CONFIG_DATA['browser'] == 'chrome':
            driver = webdriver.Chrome()
        elif CONFIG_DATA['browser'] == 'firefox':
            driver = webdriver.Firefox()
        elif CONFIG_DATA['browser'] == 'edge':
            driver = webdriver.Edge()
        driver.get(next_class['MeetingUrl'])
         # Firefox specific command
        if CONFIG_DATA['browser'] == 'firefox':
            time.sleep(5)
            keyboard.send('enter')
        time.sleep(5)
        mouse.move(CONFIG_DATA['zoom_launch_button_x'], CONFIG_DATA['zoom_launch_button_y'])
        mouse.click(button='left')
        # Firefox specific command
        if CONFIG_DATA['browser'] == 'firefox':
            time.sleep(3)
            mouse.move(CONFIG_DATA['firefox_choose_application_button_x'], CONFIG_DATA['firefox_choose_application_button_y'])
            mouse.click(button='left')
        time.sleep(1)
        mouse.move(CONFIG_DATA['zoom_open_button_x'], CONFIG_DATA['zoom_open_button_y'])
        mouse.click(button='left')

        ss.screenshot(next_class_end_time, CONFIG_DATA['zoom_position'])
        
        TODAY_CLASS_LIST.pop(0)
