import datetime
from app import db


class Customer(db.Model):
    __tablename__ = "cust"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    surname = db.Column(db.String(36))
    # email = db.Column(db.String(120))
    # credit_card_number = db.Column(db.Integer, nullable=True)
    # delivery_address = db.Column(db.PickleType) #is this right ?!?!

    def __repr__(self):
        return '<Customer {} >'.format(self.name)


class Product(db.Model):
    __tablename__ = "prod"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(36))
#     category = db.Column(db.String(16)) # ova treba da e edno od 3 ?
#     quantity = db.Column(db.Integer)
#     size = db.Column(db.String(16)) # ova treba da e edno od 4 velicini
#     price = db.Column(db.Integer)

    def __repr__(self):
        return '<Product {}>'.format(self.name)








