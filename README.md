# AutoZoom

## About

I built this script to automate my daily classes, sometimes I miss classes because I forgot or its really early in the morning.

## How it works

I scraped [Binusmaya Myclass's](https://myclass.apps.binus.ac.id/) api and get all of the class info in json format.
After that the script will pick out all the classes that match a certain criteria:

- Have the same date as today's date
- A video conference class (not a GSLC class)
- Unique (some classes are listed twice on the website for some reason)
- And hasn't ended yet

Next it will loop through all of the class list for the day, join the class with the help of [Selenium](https://www.selenium.dev/) and take screenshots every 5 minutes in case you needed for evidence of attending the class.

## Prerequisites

- Python 3.8+
- pip
- Browser (Preferably Chrome, Firefox, or chromium based Edge)
- I HIGHLY RECOMMENDS using Chrome or Edge (both derived from Chromium project), although Firefox will also work, albeit a little slower and more of a hassle to setup because it has a different flow to open external apps
- Corresponding webdriver ([Chromedriver](https://chromedriver.chromium.org/), [Geckodriver](https://github.com/mozilla/geckodriver/releases), [Edge Webdriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/))
- Extract the .exe files from the webdriver to the project path
- Notes for Microsoft Edge users, rename the exe file to MicrosoftWebDriver.exe or it will not work

## How to use

- Clone this repository
- Make sure you already have everything from the [prerequisites](https://github.com/deXOR0/AutoZoom#prerequisites) list installed
- Run setup file
  ```
  python setup.py
  ```
- You can also run it with Setup.bat or Setup Shortcut
- Start the script with this command
  ```
  python api.py
  ```
- You can also run it with AutoZoom.bat or AutoZoom Shortcut
- Copy AutoZoom Shortcut to desktop and run it from there everyday and you won't miss a single class!

## Limitations

- This script still relies on webdriver to join zoom meetings as I haven't figure out an easier way to start zoom meeting
- I'm pretty sure the screengrab module that I use is specific for windows, I need to use this one since it allows me to take local screenshots from my multi-monitor setup
- The script can't close the zoom meeting automatically as of this update, in the hope that the lecturer will close the zoom meeting after the class ends, but if that doesn't happen, the next meet will clash with the ongoing meet
- Zoom tends to have a weird behaviour in which it won't start in maximized state, making it hard to automate the closing of the meet since it changes based on size of app

## To Do

- [x] Write a setup script to automate setup process (recording mouse position, zoom screen location, etc)
- [ ] Make zoom start in maximized state
- [x] Implement auto close meet before next class
- [ ] Make the script works for Linux and macOS
- [x] Added support for multiple timezones
