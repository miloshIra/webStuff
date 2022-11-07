from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    surname = db.Column(db.String(16))
    email = db.Column(db.String(120))
    credit_card_number = db.Column(db.String(16), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    delivery_address = db.relationship("UserAddress", back_populates="user", uselist=False)

    def __repr__(self):
        return '<User:{} {}, id:{}>'.format(self.name, self.surname, self.id)


class UserAddress(db.Model):
    __tablename__ = "user_address"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    street_and_number = db.Column(db.String)
    zip_code = db.Column(db.Integer)
    city = db.Column(db.String)
    country = db.Column(db.String)

    user = db.relationship("User", back_populates="delivery_address", uselist=False)

    def __repr(self):
        return '<Street: {}.'.format(self.street_and_number)


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    category = db.Column(db.String(16))
    quantity = db.Column(db.Integer)
    size = db.Column(db.String(2))
    price = db.Column(db.Float)

    def __repr__(self):
        return '<Product:{} id:{}>'.format(self.name, self.id)


db.create_all()


@app.route('/')
def index():
    return "Hello everyone, have a nice day."


@app.route('/users/<id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        return {"error": "user not found"}, 404
    return {'id': user.id,
                     'name': user.name,
                     'surname': user.surname,
                     'email': user.email,
                     'credit_card_number': user.credit_card_number,
                     'date_created': user.timestamp,
                     "delivery_adress": {
                         "street_and_number": user.delivery_address.street_and_number,
                         "zip_code": user.delivery_address.zip_code,
                         "city": user.delivery_address.city,
                         "country": user.delivery_address.country
                     }
                     }


@app.route('/users', methods=['GET'])
def get_users():
    data = User.query.all()
    output = []
    for user in data:
        user_data = {'id': user.id,
                     'name': user.name,
                     'surname': user.surname,
                     'email': user.email,
                     'credit_card_number': user.credit_card_number,
                     'date_created': user.timestamp,
                     "delivery_adress": {
                         "street_and_number": user.delivery_address.street_and_number,
                         "zip_code": user.delivery_address.zip_code,
                         "city": user.delivery_address.city,
                         "country": user.delivery_address.country
                     }
                     }
        output.append(user_data)
    return {"users": output}


@app.route('/users', methods=['POST'])
def add_user():
    if request.json.get('credit_card_number') is not None:
        number = request.json['credit_card_number']
        if len(number) is not 16:
            return {"error": "Invalid credit card number length"}, 400
        if int(number[0]) > 6 or int(number[0]) < 4:
            return {"error": "Invalid credit card first number"}, 400
        for i in range(0, 13):
            if number[i] == number[i + 1] == number[i + 2] == number[i + 3]:
                return {"error": "Invalid credit card - 4 or more consecutive digits are the same"}, 400
    delivery_address = UserAddress(
        street_and_number=request.json['delivery_address']["street_and_number"],
        zip_code=request.json['delivery_address']["zip_code"],
        city=request.json['delivery_address']['city'],
        country=request.json['delivery_address']['country']
    )
    user = User(
        name=request.json['name'],
        surname=request.json['surname'],
        email=request.json['email'],
        credit_card_number=request.json.get('credit_card_number', None),
        delivery_address=delivery_address
        )
    db.session.add(user)
    db.session.commit()
    return "User with id {} added".format(user.id)


@app.route('/users/<id>', methods=['DELETE'])
def delete_users(id):
    user = User.query.get(id)
    if user is None:
        return {"error": "User not found"}, 404
    db.session.delete(user)
    db.session.commit()
    return "<User with id {} deleted>".format(id)


@app.route('/products/<id>')
def get_product(id):
    product = Product.query.get(id)
    if not product:
        return {"error": "product not found"}, 404
    return {'id': product.id,
            'name': product.name,
            'category': product.category,
            'quantity': product.quantity,
            'size': product.size,
            'price': product.price}


@app.route('/products', methods=['GET'])
def get_products():
    data = Product.query.order_by(Product.price.asc())
    output = []
    for product in data:
        product_data = {'id': product.id,
                        'name': product.name,
                        'category': product.category,
                        'quantity': product.quantity,
                        'size': product.size,
                        'price': product.price}
        output.append(product_data)
    return {"products": output}


@app.route('/products', methods=['POST'])
def add_product():
    size_list = ["S", "M", "L", "XL"]
    if request.json['size'] not in size_list:
        return {"error": "Invalid size"}, 400

    category_list = ["ternerki", "pizhami", "bluzi"]
    if request.json['category'] not in category_list:
        return {"error": "Invalid category"}, 400

    product = Product(
        name=request.json['name'],
        category=request.json['category'],
        quantity=request.json['quantity'],
        size=request.json['size'],
        price=request.json['price']
        )
    db.session.add(product)
    db.session.commit()
    return "User with id {} added".format(product.id), 200


@app.route('/products/<id>', methods=['DELETE'])
def delete_products(id):
    product = Product.query.get(id)

    if product is None:
        return {"error": "Product not found"}, 404
    db.session.delete(product)
    db.session.commit()
    return "<User with id {} deleted>".format(id), 200


if __name__ == '__main__':
    app.run(port=1000, debug=True)

