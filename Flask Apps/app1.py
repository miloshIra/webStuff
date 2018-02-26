import requests
from bs4 import BeautifulSoup


request=requests.get("https://www.bookdepository.com/Learning-Python-Mark-Lutz/9781449355739")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class":"sale-price"})
string_price=(element.text.strip()) # strip to remove with space, and this is the string_price
price_whole_number = string_price[0:2]
price_decimal = string_price[3:5]
price_whole=(price_whole_number + "." + price_decimal)
price=float(price_whole)

if price < 40:
    print("Buy that shit.")
    print("The current price is {}".format(price))
else:
    print("The current price is {}".format(price))
    print("Book is to expensive, try tomorrow.")
#<span class="sale-price">69,34 €</span>
