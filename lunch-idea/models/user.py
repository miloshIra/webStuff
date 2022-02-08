from flask import session, flash
from common.database import Database


class User:
    # _id should be uuid4 but functionality first "complexity" later...
    def __init__(self, username, email, password, _id=None):
        self.username = username
        self.password = password
        self.email = email

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
        else:
            flash("Your email is already in use.")

    @staticmethod
    def login_valid(email, password):
        """Check if password is correct"""
        user = User.get_by_email(email)
        if user is not None:
            return user.password == password

    @staticmethod
    def login(user_email):
        """Logs the user and populates session"""
        session['email'] = user_email
        session['username'] = User.get_by_email(user_email).username
        print(session["username"])

    def json(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

    def save_user(self):
        """Saves the user to the users collection"""
        Database.insert("users", self.json())

