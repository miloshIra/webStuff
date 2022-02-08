from flask import Flask, session, render_template, url_for, redirect, request, flash
from common.database import Database
from models.user import User


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
        flash("Wrong email or password, please try again")
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


@app.route('/idea/')
def idea():
    """This should show an idea from the database of ideas!"""
    # Should get a random idea from the database, store is in a dictionary,
    # Compare it to ides in the dictionary to avoid repetition
    # Display it in the idea template
    # Pop the stored idea
    return render_template('idea.html')

@app.route('/forgot-password', methods=['POST', 'GET'])
def forgot_password():
    return render_template('forgot-password.html')



@app.route('/logout/')
def sing_out():
    session.clear()
    print("logged out")
    print(session)
    flash("You have been logged out")
    return redirect(url_for("login_template"))


if __name__ == '__main__':
    app.run(port=1000, debug=True)
