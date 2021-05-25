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

## Setup Guide

Since some people have problem with the setup process, here's an illustrated guide to help describe the steps clearly.
- Make sure you have downloaded and place the corresponding webdriver to AutoZoom's directory. Please refer to [this link](https://github.com/deXOR0/AutoZoom#prerequisites) about webdriver types. Also note that you have to download the correct webdriver version, this should match your browser version. If you're unsure about how to this, you can find how to do it [here](https://www.computerhope.com/issues/ch001329.htm)
- Start the setup process by selecting the setup.bat script
![setup.bat](https://media.discordapp.net/attachments/846612997836505088/846613622243196928/unknown.png)
- You should be prompted with this screen below, fill in your binusmaya credentials, and select the correct options
![Setup CMD](https://cdn.discordapp.com/attachments/846612997836505088/846614843837513748/unknown.png)
- If you've correctly installed the webdriver, an instance of your browser should pop up, in this case I use chrome
![Chromedriver](https://cdn.discordapp.com/attachments/846612997836505088/846616661489877002/unknown.png)
- If you see texts like this, just ignore it, it's just the webdriver's logs. Hopefully I'll be able to suppress it on the next update
![Log](https://media.discordapp.net/attachments/846612997836505088/846616915128090634/unknown.png)
- Next, we'll have to record the Launch Meeting button on chrome. Please Note: Do Not Resize the Browser Window! Chromedriver will always start chrome in that specific size, so if you resize the window, it will mess up the coordinates. Hover your mouse on the Launch Meeting button, hit Y on the setup cmd and click enter, hold your mouse until the timer runs out, after that it will show the recorded coordinates, if you're sure its correct, click Y again to save.
![LaunchMeet](https://media.discordapp.net/attachments/846612997836505088/846618182319079424/unknown.png?width=646&height=676)
- After that, we'll have to record the Open Zoom Meetings button. The process is similar to the Launch Meet
![OpenZoom](https://media.discordapp.net/attachments/846612997836505088/846619214717648906/unknown.png)
- If you do everything correctly, it should say that the config has been saved. You can now close the setup window.
![Close](https://media.discordapp.net/attachments/846612997836505088/846619449947717632/unknown.png)

## Limitations

- This script still relies on webdriver to join zoom meetings as I haven't figure out an easier way to start zoom meeting
- I'm pretty sure the screengrab module that I use is specific for windows, I need to use this one since it allows me to take local screenshots from my multi-monitor setup

## To Do

- [x] Write a setup script to automate setup process (recording mouse position, zoom screen location, etc)
- [x] Implement auto close meet before next class
- [ ] Make the script works for Linux and macOS
- [x] Added support for multiple timezones
