import requests
import json
import datetime
import time
import mouse
import ss
import os
from selenium import webdriver

BASE = 'https://myclass.apps.binus.ac.id'
TODAY = datetime.datetime.now().strftime('%c').split(' ')
TODAY_CLASS_LIST = []
CONFIG_FILE_PATH = 'config.json'
CONFIG_DATA = {}
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
    return datetime.datetime.now() <= build_datetime(end_time)

def build_datetime(time_string, offset=0):
    '''
    Build Datetime object set to given time_string with a specified offset if provided
    '''
    time_list = [ int(x) for x in time_string.split(':') ]
    tm = datetime.datetime.now().replace(hour=time_list[0], minute=time_list[1] + offset, second=0, microsecond=0)
    return tm

if __name__ == '__main__':
    init()
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

    print(TODAY_CLASS_LIST)

    while len(TODAY_CLASS_LIST) > 0:
        next_class = TODAY_CLASS_LIST[0]
        next_class_start_time = build_datetime(next_class['StartTime'], -15)
        next_class_end_time = build_datetime(next_class['EndTime'])

        while (now := datetime.datetime.now()) < next_class_start_time:
            print(f"Next Class: {next_class['CourseTitleEn']}, Time: {next_class['StartTime']}, Now: {now}")
            time.sleep(1)
        
        print(f"Joining {next_class['CourseTitleEn']}")


        driver = webdriver.Chrome()
        driver.get(next_class['MeetingUrl'])
        time.sleep(5)
        mouse.move(CONFIG_DATA['zoom_launch_button_x'], CONFIG_DATA['zoom_launch_button_y'])
        mouse.click(button='left')
        time.sleep(1)
        mouse.move(CONFIG_DATA['zoom_open_button_x'], CONFIG_DATA['zoom_open_button_y'])
        mouse.click(button='left')

        ss.screenshot(next_class_end_time, CONFIG_DATA['zoom_position'])
        
        TODAY_CLASS_LIST.pop(0)
