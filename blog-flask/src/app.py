from src.common.database import Database
from src.models.blog import Blog
from src.models.post import Post
from src.models.user import User
from flask import Flask, render_template, request, session, make_response, redirect

app = Flask(__name__)
app.secret_key = "Ira"


@app.route('/')
def home_template():
    return render_template('home.html')


@app.route('/login')
def login_template():
    return render_template('login.html')


@app.route('/register')
def register_template():
    return render_template('register.html')


@app.before_first_request
def initialize_database():
    Database.initialize()


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


@app.route('/logout')
def logout_user():
    print(session)
    session.pop('email', default=None)
    session.pop('username', default=None)
    print(session)
    return redirect('/')


@app.route('/auth/register', methods=['POST'])
def register_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    User.register(username, email, password)
    return render_template("profile.html", email=session['email'], username=session['username'])


@app.route('/blogs/<string:user_id>')
def user_blogs(user_id=None):
    try:
        user = User.get_by_email(session['email'])
        blogs = user.get_blogs()

        return render_template("user_blogs.html", blogs=blogs, email=user.email)
    except KeyError:
        return redirect('/')


@app.route('/blogs')
def all_blogs():
    try:
        blogs = Blog.all_blogs_from_mongo()

        return render_template("all_blogs.html", blogs=blogs)
    except KeyError:
        return redirect('/')


@app.route('/blogs/new', methods=['POST', 'GET'])
def create_new_blog():
    if request.method == 'GET':
        return render_template('new_blog.html')
    else:
        title = request.form['title']
        description = request.form['description']
        user = User.get_by_email(session['email'])
        new_blog = Blog(user.email, title, description, user._id)
        new_blog.save_to_mongo()

        return make_response(user_blogs(user._id))


@app.route('/posts/<string:blog_id>')
def blog_posts(blog_id):
    blog = Blog.get_from_mongo(blog_id)
    posts = blog.get_posts()

    return render_template('posts.html', posts=posts, blog_title=blog.title, blog_id=blog._id)


@app.route('/posts/new/<string:blog_id>', methods=['POST', 'GET'])
def create_new_post(blog_id):
    if request.method == 'GET':
        return render_template('new_post.html', blog_id=blog_id)
    else:
        title = request.form['title']
        content = request.form['content']
        user = User.get_by_email(session['email'])
        new_post = Post(blog_id, title, content, user.email)
        new_post.save_to_mongo()

        return make_response(blog_posts(blog_id))


if __name__ == '__main__':
    app.run(port=1000, debug=True)