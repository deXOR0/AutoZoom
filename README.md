# AutoZoom

## About
I built this script to automate my daily classes, sometimes I miss classes because I forgot or its really early in the morning.

## How it works
I scraped my [Binusmaya Myclass's](https://myclass.apps.binus.ac.id/) api and get all of the class info in json format.
After that the script will pick out all the classes that match a certain criteria:
- Have the same date as today's date
- A video conference class (not a GSLC class)
- Unique (some classes are listed twice on the website for some reason)
- And hasn't ended yet

Next it will loop through all of the class list for the day, join the class with the help of [Selenium](https://www.selenium.dev/) and take screenshots every 5 minutes in case you needed for evidence of attending the class.

## How to use
- Clone this repository
- Install the requirements with 
    ```
    pip install -r requirements.txt
    ```
- Make a copy of the secrets_template.py and rename it as secrets.py
    ```
    cp secrets_template.py secrets.py
    ```
- Put your credentials on secrets.py
- Start the script with this command
    ```
    python api.py
    ```
- You can also use the included shortcut
- Every screen is different, so you have to adjust your mouse position for zoom join button, use the included record.py script to record the mouse position
- Adjust zoom screen location (Monitor 1 or 2)

## Prerequisites
- Python 3.8+
- pip
- Browser (Preferably Chrome, Firefox, or chromium based Edge)
- Corresponding webdriver ([Chromedriver](https://chromedriver.chromium.org/), [Geckodriver (Firefox)](https://github.com/mozilla/geckodriver/releases), [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/))

## Limitations
- This script still relies on webdriver to join zoom meetings as I haven't figure out an easier way to start zoom meeting
- I'm pretty sure the screengrab module that I use is specific for windows, I need to use this one since it allows me to take local screenshots from my multi-monitor setup
- The script can't close the zoom meeting automatically as of this update, in the hope that the lecturer will close the zoom meeting after the class ends, but if that doesn't happen, the next meet will clash with the ongoing meet
- Zoom tends to have a weird behaviour in which it won't start in maximized state, making it hard to automate the closing of the meet since it changes based on size of app

## To Do
- Write a setup script to automate setup process (recording mouse position, zoom screen location, etc)
- Make zoom start in maximized state
- Implement auto close meet before next class
- Make the script works for Linux and macOS
