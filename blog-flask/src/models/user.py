import datetime
import uuid
from flask import session
from src.common.database import Database
from src.models.blog import Blog


class User:
    def __init__(self, username, email, password, _id=None):
        self.username = username
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("users", {"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password

        return False

    @classmethod
    def register(cls, username, email, password):
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(username, email, password)
            new_user.save_to_mongo()
            session['email'] = email
            session['username'] = username
            return True
        else:
            return False

    @staticmethod
    def login(user_email):
        session['email'] = user_email
        session['username'] = User.get_by_email(user_email).username
        print(session["username"])

    @staticmethod
    def logout():
        session['email'] = None
        session['username'] = None

    def get_blogs(self):
        return Blog.find_by_author_id(self._id)

    def new_blog(self, title, description):
        blog = Blog(author=self.email,
                    title=title,
                    description=description,
                    author_id=self._id)

        blog.save_to_mongo()

    @staticmethod
    def new_post(blog_id, title, content, date=datetime.datetime.utcnow()):
        blog = Blog.get_from_mongo(blog_id)
        blog.new_post(title=title,
                      content=content,
                      date=date)

    def json(self):
        return {
            "username": self.username,
            "email": self.email,
            "_id": self._id,
            "password": self.password
        }

    def save_to_mongo(self):
        Database.insert("users", self.json())

