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



# use fullstack
# db.users.insert({"_id": "123", "email": "Iradan123@gmail.com", "password": "$pbkdf2-sha256$7665$WKs1ZkwJ4ZxT6t07R0iplQ$ZKfMMAMzKxH64g.3XwaFONAlVwoZf76dWdqW6uSlQtE"})
# db.items.insert({"_id": "d5527d22c0a74a8199fbbc0aab44046", "url": "https://www.bookdepository.com/Learning-Python-Mark-Lutz/9781449355739?ref=grid-view&qid=1525427233471&sr=1-1", "name": "Learning Python" })
# db.alerts.insert({"_id": "896045e647084cacb37a702f418be70", "price_limit": 100, "last_checked": ISODate("2016-02-09T10:35:31.542Z"), "item_id": "d5527d22c0a74a8199fbbc0aab440463", "user_email": "iradan123@gmail.com"})
# db.stores.insert({ "_id" : "253217ddddf74923852cf3f84f9b48b8", "name" : "Book Depository", "url_prefix" : "https://www.bookdepository.com", "tag_name" : "span", "query" : { "class" : "sale-price" } })
