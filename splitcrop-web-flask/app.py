from flask import Flask, render_template, request, session, redirect, url_for
from models.user import User
from common.database import Database
import main
import time
from PIL import Image
import random


app = Flask(__name__)
app.secret_key = "Ira"


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.before_request
def make_session_permanent():
    session.permanent = True


@app.route('/')
def start_template():
    return render_template('index.html')


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/auth-register', methods=['POST', 'GET'])
def register_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    print(username, email, password)
    User.register(username, email, password)
    return render_template("index.html")


@app.route('/auth/login', methods=['POST', 'GET'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None
        return render_template("wrong_login.html")

    # return render_template("home.html", email=session['email'], username=session['username'])
    print(session)
    return redirect(url_for('home_template'))


@app.route('/home')
def home_template():
    if "username" not in session:
        return redirect(url_for('start_template'))
    return render_template('home.html')


@app.route('/split', methods=['POST', 'GET'])
def split_image():
    if request.method == 'POST':
        image = request.files['image']
        image = Image.open(image)
        image_parts = main.split_to_three(image)  # remnants of the past..
        return render_template("split.html")
        # return send_from_directory(".", image_parts[0])
    else:
        return render_template('split.html')
    # if request.form['divide_count'] == 2:
    #     main.split_to_two(image)
    # elif request.form['divide_count'] == 3:
    #     main.split_to_three(image)
    # elif request.form['divide_count'] == 6:
    #     main.split_to_six(image)

    # general login of how it should work, just a quick idea need to add a lot of stuff.


@app.route('/login')
def login_template():
    return render_template('login.html')


@app.route('/forgot-password', methods=['POST', 'GET'])
def forgot_password():
    return render_template('forgot-password.html')


@app.route('/reset-password', methods=['POST'])
def reset_password():
    if request.method == 'POST':
        global reset_email
        reset_email = request.form['email']
        if User.get_by_email(reset_email) is not None:
            token = random.randint(100000, 999999)
            User.save_reset_token(reset_email, token, time.time())
            return render_template("/reset-password.html")
        else:
            return "No such email"


@app.route('/change-password', methods=['POST', 'GET'])
def change_password():
    # Add time attribute to the input so Mongo can recognize it and then arrange them by date.
    try:
        user_data = User.get_reset_token(reset_email)
        user_input_token = int(request.form['token'])
        print(user_data['time'])
        if user_input_token == user_data['token'] and time.time() - user_data['time'] < 60:
            return render_template('new-password.html')
        else:
            return "The code is wrong or has expired please go back and try again"
    except ValueError:
        return "The code is wrong or has expired please go back and try again"


@app.route('/new-password', methods=['POST'])
def set_new_password():
    new_password_once = request.form['new_password_once']
    new_password_twice = request.form['new_password_twice']
    if new_password_once == new_password_twice:
        User.update_password(reset_email, new_password_once)
        return redirect(url_for('start_template'))
    else:
        return "Passwords don't match please go back and try again."


@app.route('/signout/')
def sing_out():
    session.clear()
    print("logged out")
    print(session)
    return redirect("/")


if __name__ == '__main__':
    app.run(port=2000, debug=True)
