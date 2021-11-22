import requests
from bs4 import BeautifulSoup


URL = "https://www.anhoch.com/product/44821/smartwatch-ldk-d900-blue-kids-touchgpslbs-locationsimsos-callflashlightcamerawaterproof"
TAG_NAME = "span"
QUERY = {"class": "nm"}

response = requests.get(URL)
print("hello")
content = response.content
soup = BeautifulSoup(content, "html.parser")
elements = soup.find(TAG_NAME, QUERY)
string_prince = elements.text
print(string_prince)



#print(response.content)
