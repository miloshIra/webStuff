import uuid
import models.users.errors as UserErrors
from common.utils import Utils
from common.database import Database
from models.alerts.alert import Alert

class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)


    @staticmethod
    def is_login_valid(email, password):
        """
        This method verifies that an email/password combo sent is valid or not.
        Checks that the email and the pass associeted with the email is corret
        :param email: the user's email
        :param password: A sha512 hashed password
        :return: True if valid, False otherwise
        """
        user_data = Database.find_one('users', {"email":email}) # password in sha512 -> pbkdf2_sha512
        if user_data is None:
            # Tell the user email does not exist
            raise UserErrors.UserNotExistsError("Your user does not exist.")
        if not Utils.check_hashed_password(password, user_data['password']):
            # Tell the user their password is wrong
            raise UserErrors.IncorrectPasswordError("Your password was wrong.")

        return True

    @staticmethod
    def register_user(email, password):
        """
        This method registers a user using email and password, the password comes hashed as sha-512
        """
        user_data = Database.find_one('users', {"email":email})

        if user_data is not None:
            raise UserErrors.UserAlreadyRegistered("The email you used to register already exists.")

        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError("The e-mail does not have the right format.")

        User(email, Utils.hash_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert("users", self.json())

    def json(self):
        return {
            "_id":self._id,
            "email":self.email,
            "password":self.password
        }

    @classmethod
    def find_by_email(cls, email):
        return cls(**Database.find_one('users', {'email': email}))

    def get_alerts(self):
        return Alert.find_by_user_email(self.email)
