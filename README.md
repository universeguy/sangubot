# sangubot
Python script to automate form filling for UOL results while notifying the release of results. This tutorial will go over the creation of a new Telegram bot for your Telegram group, and the further configuration to link it up with the script to get notifications The idea of this script is to automate tedious process of repeatedly the filling out the details to check if the results for the academic year is out. The form will be filled out and submitted every **5 minutes**.

# Getting started
Firstly, the `credentials.py has` to be filled in with one's credentials before running `results.py`.
Breakdown is as follows:

- bot_token

<p>This can be obtained through @botfather on Telegram. Upon starting a chat with @BotFather, type `/newbot` to start the process of creating a new bot. Give your bot a name and an unique ID. Following that, BotFather will be provide you with the token. Use this token in `credentials.py` to link up the bot and `results.py` script.</p>

- bot_chatID

<p>Assuming you want a bot to notify you and your coursemates in a group, you have to get the ID of the group chat that your bot is a a part of. Add @getmyid_bot as a new number into your target group, and copy the chat ID into credentials.py</p>

- username

<p>Replace with your UOL VLE login, e.g. `'mhk12'`</p>

- candidate_no

<p>Replace with your Admission Notice candidate number, e.g. `'N38291'`</p>

- day

<p>Birthday (DD), `'2'` if you're born on the 2nd.</p>

- month

<p>Birthmonth (MM/M), `'1'` if your birthmonth is January.</p>

- year

Birthyear (YYYY)

Secondly, 
Python has to be installed on your machine, from https://www.python.org/downloads/. Make sure python is set as an environment variable for your terminal/command prompt, this option can be found at the end of the Python setup. Once done, open a command prompt at your local version of this project (folder which contains credentials.py, results.py and requirements.txt) and enter this into your command prompt/terminal: `pip install -r requirements.txt` This will proceed to install all libraries needed for this script.

Finally, to run the script, type this: `python results.py`

# Acknowledgments
This script is just an updated version of [Phone's version](https://github.com/phonethantko/uolresults2018). Documentations of the various libaries were of tremendous help as well.

# Disclaimer
Please take note that this script has to be run on your own risk, be responsible for your own credentials and data. The interval has been set to a safe period of 5 minutes to avoid any issues with request issues.
