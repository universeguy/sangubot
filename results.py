import mechanicalsoup, requests, time
from bs4 import BeautifulSoup
import requests
import my_credentials

def send_message_to_bot(msg):
    send_text = 'https://api.telegram.org/bot' + my_credentials.bot_token + '/sendMessage?chat_id=' + my_credentials.bot_chatID + '&parse_mode=Markdown&text=' + msg
    requests.get(send_text) # using a webhook to send a message through the telegram bot. simplest way to get a bot to talk

def complete_form():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://results.londoninternational.ac.uk/examresults/results.do")

    # first page to enter username
    form = browser.select_form() #selecting the only form in the page
    browser['login.username'] = my_credentials.username # entering into field with username set earlier
    response = browser.submit_selected() # submitting form with the only button that's available in the whole page

    # second page loaded
    form = browser.select_form() # selecting the only form in the page
    browser["login.candnum"] = my_credentials.candidate_no # entering into field with candidate_no set earlier
    browser["login.dobday"] = my_credentials.day # entering into field with birthday set earlier
    browser["login.dobmonth"] = my_credentials.month # entering into field with birthmonth set earlier
    browser["login.dobyear"] = my_credentials.year # entering into field with birthyear set earlier
    form.choose_submit('validate') # submitting form using the last button found in the page, named 'validate'. 
    # will not work if JUST browser.submit_selected() is done as there are two submit buttons in this page 'change' and 'submit'
    response = browser.submit_selected()
    web_content = BeautifulSoup(response.text, 'lxml') # scraping the final webpage that I end up with after entering my correct credentials
    # take note that until 2018/19 resutls are out, 2017/18 results and the respective older candidate no. will be shown in the results page

    if my_credentials.candidate_no in str(web_content): # if final page consists of results with the current year's candidate no. (not previous year's), it's time
        send_message_to_bot("Hey guys, results are out! Y'all might wanna check it. All the best to everyone!")
        exit(0) # kills whole script and bot as well, since work is done

    else: # anything else, falls under this condition
        send_message_to_bot("Results are not out yet, chill & have one more shot of whiskey.")

    time.sleep(300) # 5mins interval so that UOL international's website doesn't end up with a DoS attack or something...

while True:
    complete_form() # calling the method until exit(0) happens when results are out