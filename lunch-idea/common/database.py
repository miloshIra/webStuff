# DATABASE CLASS
import pymongo


class Database:
    """ The database class """
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['LunchIdea']

    # @staticmethod
    # def count_entries(collection):
    #     Database.DATABASE[collection].countDocuments()

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    # is find == find_all() ?? check later ..

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def find_token(collection, query):
        return Database.DATABASE[collection].find(query).sort('time', -1).limit(1)[0]

    @staticmethod
    def update_password(collection, finder, query):
        Database.DATABASE[collection].update_one(finder, query)

    @staticmethod
    def delete(collection, query):
        Database.DATABASE[collection].remove(query)
