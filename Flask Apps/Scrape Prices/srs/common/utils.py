from passlib.hash import pbkdf2_sha512
import re

class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile('^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def hash_password(password):
        """
        Hashes password using pbkdf2_sha512
        return: A sha512 > pbkdf2)sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)


    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Check that the password user sent matches the database one.
        The database password is encrypted more than the user's passowrd at this stage.
        password: sha512 hashed password
        hashed_password : pbkdf2_sha512 encrypted password
        return True if password match, false otherwise
        """
        return pbkdf2_sha512.verify(password, hashed_password)
