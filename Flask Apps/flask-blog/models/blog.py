import uuid


class Blog:
    def __init__(self, author, title, description, id=None):
        pass
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        pass

    def get_posts(self):
        pass

    def save_to_mongo(self):
        pass

    def json(self):
        pass

    def get_from_mongo(self):
        pass

    