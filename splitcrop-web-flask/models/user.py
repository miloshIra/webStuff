from flask import session
from common.database import Database


class User:
    def __init__(self, username, email, password, _id=None):
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def register(cls, username, email, password):
        user = cls.get_by_email(email)
        print(user)
        if user is None:
            new_user = cls(username, email, password)
            new_user.save_user()
            # session['email'] = email
            # session['username'] = username
            return True
        else:
            return False  # but why tho ???

    def json(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

    def save_user(self):
        Database.insert("users", self.json())