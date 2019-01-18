import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time
from variables import *
import html2text

url = input("URL of website you want to scrape: ")
client = Client(accnt_sid, auth_tkn)
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
text = str(soup)
siteText = html2text.html2text(text)

print("Page content: \n " + str(siteText))
interval = int(input("How long do I wait before checking again each time (seconds)? : "))
if(interval < 15):
    print("Cannot input a number less than 15. Setting interval time to 15 seconds.")
    interval = 15
numChecks = int(input("How many times do you want me to check this website? : "))
cancel_after_success = str(input("Do you want to cancel the process after 1 successful check? [y/n] : "))
if(cancel_after_success == "y") or (cancel_after_success == "Y"):
    cancel_after_success == True
elif (cancel_after_success == "n") or (cancel_after_success == "N"):
    cancel_after_success == False
else:
    print("That is not a valid input")

def findChange():
    client = Client(accnt_sid, auth_tkn)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    text = str(soup)
    siteText = html2text.html2text(text)
    countChecks = 0
    while True:
        countChecks += 1
        print("Number of checks " + str(countChecks))
        newPage = requests.get(url)
        newSoup = BeautifulSoup(newPage.content, "html.parser")
        newText = str(newSoup)
        newSiteText = html2text.html2text(newText)
        if(newSiteText != siteText):
            client.messages.create(
                body = "The page has changed since I last checked", 
                to = myNum, 
                from_ = twilioNum
                )
            if(cancel_after_success):
                print("Message sent, process canceled")
                break
            else:
                if(countChecks >= numChecks):
                    print("Max number of checks reached, process canceled")
                    break
                else:
                    print("Message sent, process running")
                    time.sleep(interval)
                    continue
        elif(newSiteText == siteText):
            client.messages.create(
                body = "No changes were detected",
                to = myNum,
                from_ = twilioNum
                )
            if(cancel_after_success):
                print("Message sent, process canceled")
                break
            else:
                if(countChecks >= numChecks):
                    print("Max number of checks reached, process canceled")
                    break
                else:
                    print("Message sent, process running")
                    time.sleep(interval)
                    continue
        else:
            if(countChecks >= numChecks):
                print("Max number of checks reached, process canceled")
                break
            client = Client(accnt_sid, auth_tkn)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            text = str(soup)
            siteText = html2text.html2text(text)
            continue

findChange()
