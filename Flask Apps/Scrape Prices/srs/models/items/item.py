import uuid
import requests
from bs4 import BeautifulSoup
import re
import models.items.constants as ItemConstants
from models.stores.store import Store
from common.database import Database

class Item(object):
    def __init__(self, name, url, _id=None):
        self.name = name
        self.url = url
        store = Store.find_by_url(url)
        tag_name = store.tag_name
        query = store.query
        self.price = self.load_price(tag_name, query)
        self._id = uuid.uuid4().hex if _id is None else _id


    def __repr__(self):
        return "<Item {} with URL {}".format(self.name, self.url)

    def load_price(self, tag_name, query):
        # <span class="a-size-medium a-color-price header-price">$31.24</span>
        request = requests.get(self.url)
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(tag_name, query)
        string_price = element.text.strip()

        pattern = re.compile("(\d+,\d+)") # 155.00
        match = pattern.search(string_price)

        return match.group()

    def save_to_mongo(self):
        Database.insert(ItemConstants.COLLECTION, self.json())
        # Insert JSON representation
        pass

    def json(self):
        return {
            "name": self.name,
            "url": self.url,
            "_id": self._id
        }
