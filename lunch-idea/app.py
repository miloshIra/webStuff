from flask import Flask, session, render_template, url_for, redirect, request, flash
from common.database import Database
from models.user import User
from models.idea import LunchIdea
import random
import time


app = Flask(__name__)
app.secret_key = "Key"  # Should of be changed later.


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.before_request
def make_session_permanent():
    session.permanent = True   # Should make session permanent .. but we shall see.


@app.route('/')
def home():
    if 'username' in session:  # 'username' Should change to if session[used_id] is None maybe ..
        return render_template('idea.html')
    else:
        return redirect(url_for('login_template'))


@app.route('/user-profile/')
def profile():
    return render_template('profile.html')


@app.route('/idea/')
def idea():
    """This should show an idea from the database of ideas!"""
    latest_ideas = []
    current_idea = LunchIdea.get_idea("tradicionalna")  # tradicionalna* should come for a radio button on the template
    if current_idea not in latest_ideas:
        latest_ideas.append(current_idea)
        idea = current_idea
    else:
        pass
    # Should get a random idea from the database, store is in a dictionary,
    # Compare it to ides in the dictionary to avoid repetition
    # Display it in the idea template
    # Pop the stored idea
    return render_template('idea.html', idea=current_idea)


# USER AUTH TEMPLATES

@app.route('/login/')
def login_template():
    return render_template('login.html')


@app.route('/register/')
def register_template():
    return render_template('register.html')


@app.route('/auth/login', methods=['POST', 'GET'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None
        flash("Wrong email or password, please try again.")
        return redirect(url_for('login_template'))

    # return render_template("home.html", email=session['email'], username=session['username'])
    print(session)
    return redirect(url_for('profile'))


@app.route('/register/auth-register', methods=['POST', 'GET'])
def register_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    print(username, email, password)

    User.register(username, email, password)

    return redirect(url_for('login_template'))


@app.route('/forgot-password', methods=['POST', 'GET'])
def forgot_password():
    return render_template('forgot-password.html')


@app.route('/reset-password', methods=['POST'])
def reset_password():
    # if request.method == 'POST':
    #     global reset_email
    reset_email = request.form['email']
    if User.get_by_email(reset_email) is not None:
        token = random.randint(100000, 999999)
        User.save_reset_token(reset_email, token, time.time())
        return render_template("/reset-password.html", email=reset_email)
    else:
        flash("No such email, please register.")
        return redirect(url_for('register_template'))


@app.route('/change-password', methods=['POST', 'GET'])
def change_password():
    # Add time attribute to the input so Mongo can recognize it and then arrange them by date.
    # It doesnt work now cause it only checks first token and it's usually is expired.
    # Well it does work but only if there is 1 token in the database.
    reset_email = request.form['email']
    user_data = User.get_reset_token(reset_email)
    user_input_token = int(request.form['token'])
    print(user_data['time'])
    if user_input_token == user_data['token'] and time.time() - user_data['time'] < 60:
        return render_template('new-password.html',  email=reset_email)
    else:
        flash("The code is wrong or has expired please go back and try again")
        return redirect(url_for('reset_password'))


@app.route('/new-password', methods=['POST'])
def set_new_password():
    reset_email = request.form['email']
    new_password_once = request.form['new_password_once']
    new_password_twice = request.form['new_password_twice']
    if new_password_once == new_password_twice:
        User.update_password(reset_email, new_password_once)
        flash("Password changed, please log in.")
        return redirect(url_for('login_template'))
    else:
        flash("Passwords don't match please go back and try again")


@app.route('/logout/')
def sing_out():
    session.clear()
    print("logged out")
    print(session)
    flash("You have been logged out")
    return redirect(url_for("login_template"))


if __name__ == '__main__':
    app.run(port=1000, debug=True)

# TODO 1: Populate the idea mongodb collection with few ideas and display a random one in the idea template,
#  as described in the app.py and idea.html.
# TODO 2: Work on weekly list of ideas and how to generate a shopping list from their ingredients.
# TODO 3: Make flask-mail work!
# TODO 4. Protect endpoints from not logged users.
# TODO 5. Enjoy life more.
