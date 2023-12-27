import os, time, pywhatkit
import pyautogui
from Face.Ear import understand
from Face.Mouth import speak
import webbrowser
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes = .0)).strftime("%M"))
contacts = {
    "myself": "+916291528931",
    "suravi": "+917908329678",
    "pratibha": "+919749756954",
    "sandipan": "+919051152279"
}
def send_msg():
    speak("Who do you want to msg?")
    print("Contacts List:")
    for x in contacts.keys():
        print(f"{x}")

    name = input("Enter name from list: ")
    if name in contacts:
        speak("What's the msg?")
  
        msg = input("Enter: ")

        pywhatkit.sendwhatmsg(f"{contacts[name]}",msg,time_hour=00,
        time_min=16)

    else:
        pass

# send_msg()
