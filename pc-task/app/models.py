from app import db
import datetime


class User(db.Model):
    """This is the Customer/User customer class, used User as name because it is shorter """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    surname = db.Column(db.String, index=True)
    # email = db.Column(db.String, index=True)
    # timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # delivery_address = db.Column(db.String) # Should be a dictionary ??

    def __repr__(self):
        return '<User {}>'.format(self.name)


