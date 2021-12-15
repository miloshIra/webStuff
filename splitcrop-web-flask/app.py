from flask import Flask, render_template, request, session, make_response, redirect
from models.user import User
from common.database import Database


app = Flask(__name__)
app.secret_key = "Ira"


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/', methods=['POST', 'GET'])
def start_template():
    return render_template('index.html')


@app.route('/auth-register', methods=['POST', 'GET'])
def register_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    print(username, email, password)
    User.register(username, email, password)
    return render_template("index.html")



@app.route('/home')
def home_template():
    return render_template('home.html')


@app.route('/login')
def login_template():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(port=1000, debug=True)
