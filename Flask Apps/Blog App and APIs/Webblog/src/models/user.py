from common.database import Database
from models.blog import Blog
from flask import Flask, session
import datetime


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls):
        data = Database.find_one("users", {"_id": _id})
        if data is not None:
            return cls(**data)
        pass

    @staticmethod
    def login_valid(email, password):
        # Check if email is valid with password.
        user = User.get_by_email(email)
        if user is not None:
            #Check password
            return user.password == password
        return False

    @classmethod
    def register(cls, email, password):
        user = cls.get_by_email(email)
        if user is None:
            # User does not exist, so we create find_one
            new_user = cls(email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            # User exists
            return False

    @staticmethod
    def login(user_email):
        # loing_valid has already been called
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None


    def get_blogs(self):
        return Blog.find_by_author_id(self._id)

    def new_blog(self, title, description):
        blog = Blog(author=self.email,
            title=title,
            description=description,
            author_id=self._id)

        blog.save_to_mongo()

    @staticmethod
    def new_post(blog_id, title, content, date=datetime.datetime.now()):
        blog = Blog.from_mongo(blog_id)
        blog.new_post(title=title, content=content, data=date)


    def json(self):
        return {
        "email": self.email,
        "_id": self._id,
        "password": self.password
        }


    def save_to_mongo():
        Database.insert("users", self.json())
