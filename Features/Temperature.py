import requests
from bs4 import BeautifulSoup

def check_temperature(command):
    command = command.replace("nemo ","")
    command = command.replace("search ","")
    url = f"https://www.google.com/search?q={command}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    return f"Current temperature is {temp}"