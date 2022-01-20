from flask import session
from common.database import Database


class User:
    def __init__(self, username, email, password, _id=None):
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def get_by_email(cls, email):
        """Check the database for a user by email"""
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def register(cls, username, email, password):
        """Registers users, by checking database if it exists, and if not it adds the user"""
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

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password

    @staticmethod
    def login(user_email):
        session['email'] = user_email
        session['username'] = User.get_by_email(user_email).username
        print(session["username"])

    @staticmethod
    def save_reset_token(email, token):
        Database.insert("tokens", {"email": email, "token": token})

    @staticmethod
    def get_reset_token(email):
        data = Database.find_one("tokens", {"email": email})
        if data is not None:
            return data

    @staticmethod
    def update_password(email, password):
        Database.update_password("users", {"email": email}, {"$set": {"password": password}})

    def json(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

    def save_user(self):
        Database.insert("users", self.json())
