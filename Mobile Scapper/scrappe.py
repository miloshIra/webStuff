from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.ui import Select

def load_countries():
    global z
    request = requests.get("https://mobilerecharge.com/buy/mobile_recharge?country=Afghanistan&operator=Etisalat")
    content = request.content
    # print(content)
    soup = BeautifulSoup(content,"html.parser")
    state = soup.find("select", {"id":"international_country"})
    count = (state.text.strip()).split()
    z = count[2:]
load_countries()
print(z)


driver = webdriver.Chrome()
driver.get("https://mobilerecharge.com/buy/mobile_recharge?country=Afghanistan&operator=Etisalat")

def list_contries():

    select = Select(driver.find_element_by_id('international_country'))
    select.select_by_visible_text('France')
    request = requests.get("https://mobilerecharge.com/buy/mobile_recharge?country=Afghanistan&operator=Etisalat")
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    prov = soup.find("div", {"id":"data-operator_name"})
    operator = (prov.text.strip())
    print(operator)

list_contries()
