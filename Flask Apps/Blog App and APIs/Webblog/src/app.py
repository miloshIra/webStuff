from flask import Flask, render_template, request, session
from models.user import User
from common.database import Database


app = Flask(__name__) #'__main__'
app.secret_key="Ira"

@app.route('/')
def home_template():
    render_template('home.html')

@app.route('/login') # localhost:4995/login
def login_template():
    return render_template('login.html')

@app.route('/register') # localhost:4995/register
def register_template():
    return render_template('login.html')

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/auth/login', methods=['POST'])

def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email']=None

    return render_template("profile.html", email=session['email'])

@app.route('/auth/register', methods=['POST'])

def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register_user(email,password)
    return render_template("profile.html", email=session['email'])

if  __name__=='__main__':
    app.run(port=4995)
