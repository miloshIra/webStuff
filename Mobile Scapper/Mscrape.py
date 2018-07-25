from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

def load_countries():
    request = requests.get("https://mobilerecharge.com/")
    content = request.content
    # print(content)
    soup = BeautifulSoup(content,"html.parser")
    state = soup.find("select", {"id":"international_country"})
    count = (state.text.strip()).split()
    zemji = count[2:]
    print(zemji)


# print(list_of_countries)

load_countries()


driver = webdriver.Chrome()
driver.get("https://mobilerecharge.com/")
