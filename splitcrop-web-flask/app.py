from flask import Flask, render_template, request, session, make_response, redirect, send_from_directory
from models.user import User
from common.database import Database
import main
from PIL import Image
import time


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


@app.route('/auth/login', methods=['POST', 'GET'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
        print(session)
    else:
        session['email'] = None
        return render_template("wrong_login.html")

    return render_template("home.html", email=session['email'], username=session['username'])
    # return redirect("/", email=session['email'], username=session['username'])


@app.route('/home')
def home_template():
    return render_template('home.html')


@app.route('/split', methods=['POST', 'GET'])
# @login_required
def split_image():
    if request.method == 'POST':
        print(request.files)
        image = request.files['image']
        image = Image.open(image)
        image_parts = main.split_to_three(image)
        # time.sleep(5000)
        print(session)
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
        email = request.form['email']
        if User.get_by_email(email) is not None:
            print(email)
            return redirect("/")
        else:
            return "No such email"


if __name__ == '__main__':
    app.run(port=1000, debug=True)
