# AutoZoom

## About

I built this script to automate my daily classes, sometimes I miss classes because I forgot or it's early in the morning.

## What's New

-   You can now change the screenshot interval to your liking in the setup, or even turn it off completely!
-   Restructured project so it looks cleaner and more user-friendly

## How it works

I scraped [Binusmaya Myclass's](https://myclass.apps.binus.ac.id/) API and got all of the class info in JSON format.
After that, the script will pick out all the classes that match certain criteria:

-   Have the same date as today's date
-   A video conference class (not a GSLC class)
-   Unique (some classes are listed twice on the website for some reason)
-   And hasn't ended yet

Next, it will loop through the class list for the day, join the class with the help of [Selenium](https://www.selenium.dev/), and take screenshots every a certain number of minutes in case you need it for evidence of attending the class. You can set this interval on the setup process, as well as opting to not take any screenshots at all by setting the interval to 0.

## Prerequisites

-   Python 3.8+
-   pip
-   Browser (Preferably Chrome, Firefox, or Chromium-based Edge)
-   I HIGHLY RECOMMENDS using Chrome or Edge (both derived from the Chromium project), although Firefox will also work, albeit a little slower and more of a hassle to setup because it has a different flow to open external apps
-   Corresponding webdriver ([Chromedriver](https://chromedriver.chromium.org/), [Geckodriver](https://github.com/mozilla/geckodriver/releases), [Edge Webdriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/))
-   Extract the .exe files from the webdriver to the webdriver directory
    ![Webdriver Directory](https://cdn.discordapp.com/attachments/846612997836505088/893153577009311805/unknown.png?ex=6617fe16&is=66058916&hm=8fd983e2dd388f3512e6134d9b2db23000d7babb1e86843076dcba64e532f50a&)
-   Notes for Microsoft Edge users, rename the exe file to MicrosoftWebDriver.exe or it will not work

## Setup Guide

Since some people have problems with the setup process, here's an illustrated guide to help describe the steps clearly.

-   Make sure you have downloaded and placed the corresponding webdriver in AutoZoom's directory. Please refer to [this link](https://github.com/deXOR0/AutoZoom#prerequisites) about webdriver types. Also, note that you have to download the correct Webdriver version, this should match your browser version. If you're unsure about how to do this, you can find how to do it [here](https://www.computerhope.com/issues/ch001329.htm)
-   Start the setup process by selecting the setup.bat script
    ![setup.bat](https://cdn.discordapp.com/attachments/846612997836505088/893152695450480680/unknown.png?ex=6617fd44&is=66058844&hm=b9812bbaf3796451e2c67b9bfd28e67661666aeedf9dba20f14969f8bf4f604e&)
-   You should be prompted with this screen below, fill in your binusmaya credentials, and select the correct options
    ![Setup CMD](https://cdn.discordapp.com/attachments/846612997836505088/846614843837513748/unknown.png?ex=661e0704&is=660b9204&hm=03af47d99680c86200351e0cb5e481c102bc0804386362b666805fd1a718ccae&)
-   If you've correctly installed the webdriver, an instance of your browser should pop up, in this case, I use Chrome
    ![Chromedriver](https://cdn.discordapp.com/attachments/846612997836505088/846616661489877002/unknown.png?ex=661e08b5&is=660b93b5&hm=408b04cef54d9b7502b0e37f3eb591615e25875ceacbbf54e20defbd20e20e2c&)
-   If you see texts like this, just ignore it, it's just the webdriver's logs. Hopefully, I'll be able to suppress it on the next update
    ![Log](https://cdn.discordapp.com/attachments/846612997836505088/846616915128090634/unknown.png?ex=661e08f1&is=660b93f1&hm=b160ec5bb0019ce41d57c8c44f5034d7087ae077ac0af69064ce18fd9facdb10&)
-   Next, we'll have to record the Launch Meeting button on Chrome. Please Note: Do Not Resize the Browser Window! Chromedriver will always start Chrome in that specific size, so if you resize the window, it will mess up the coordinates. Hover your mouse on the Launch Meeting button, hit Y on the setup cmd, and click enter, hold your mouse until the timer runs out, after that it will show the recorded coordinates, if you're sure it's correct, click Y again to save.
    ![LaunchMeet](https://cdn.discordapp.com/attachments/846612997836505088/846618182319079424/unknown.png?ex=661e0a20&is=660b9520&hm=c2f32c8d84e171b0507f7d9b37c0c4cd5563338f998ba2011209770bc76b3c89&)
-   After that, we'll have to record the Open Zoom Meetings button. The process is similar to the Launch Meet
    ![OpenZoom](https://cdn.discordapp.com/attachments/846612997836505088/846619214717648906/unknown.png?ex=661e0b16&is=660b9616&hm=77c9285b89d1bc98bfa7539720a24502a5039502aa79949d8bc0e70ade454140&)
-   If you do everything correctly, it should say that the config has been saved. You can now close the setup window.
    ![Close](https://cdn.discordapp.com/attachments/846612997836505088/846619449947717632/unknown.png?ex=661e0b4e&is=660b964e&hm=2dc1b8e3fcf6a4eab9c7fce369caf26c10779cfd467d9a7ccf0ba6e4763d6c72&)

## Zoom Settings

-   In order to fully utilize AutoZoom, you can use the settings below. Note that this is optional, but I highly recommend it.
    ![ShareScreen](https://cdn.discordapp.com/attachments/846612997836505088/846621150926340106/unknown.png?ex=661e0ce3&is=660b97e3&hm=0f2c97ed7b62ec2fb622ec82447084aa130084e9f5400d8c1eee6f59a0e28d0f&)
    ![Shortcuts](https://cdn.discordapp.com/attachments/846612997836505088/846621260863373322/unknown.png?ex=661e0cfe&is=660b97fe&hm=389396c986fe6ba354e20c50431069005ed932461b866a05b922cb5ae9908b70&)

## How to use

-   Clone this repository
-   Make sure you already have everything from the [prerequisites](https://github.com/deXOR0/AutoZoom#prerequisites) list installed
-   Run the setup file
    ```
    python setup.py
    ```
-   You can also run it with Setup.bat or Setup Shortcut
-   Start the script with this command
    ```
    python api.py
    ```
-   You can also run it with AutoZoom.bat or AutoZoom Shortcut
-   Copy AutoZoom Shortcut to your desktop and run it from there every day and you won't miss a single class!

## Limitations

-   This script still relies on Webdriver to join Zoom meetings as I haven't figured out an easier way to start Zoom meeting
-   I'm pretty sure the screengrab module that I use is specific for Windows, I need to use this one since it allows me to take local screenshots from my multi-monitor setup

## To Do

-   [x] Write a setup script to automate the setup process (recording mouse position, zoom screen location, etc)
-   [x] Implement auto close meet before next class
-   [ ] Make the script work for Linux and macOS
-   [x] Add support for multiple timezones
-   [x] Add support to join custom Zoom meetings
