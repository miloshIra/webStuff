import requests
from bs4 import BeautifulSoup
import re

request = requests.get("https://www.bookdepository.com/Learning-Python-Mark-Lutz/9781449355739?ref=grid-view&qid=1523899750611&sr=1-1")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class":"sale-price"})
string_price = element.text.strip()

pattern = re.compile("(\d+,\d+)") # 155.00
match = pattern.search(string_price)

print(match.group())
