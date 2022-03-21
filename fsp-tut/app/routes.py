from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ira'}
    posts = [
        {
            'author': {'username': 'Ira'},
            'body':'Beautiful day in Skopje'
        },
        {
            'author': {'username':'Poky'},
            'body': 'Great morning somewhere'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Log in', form=form)

