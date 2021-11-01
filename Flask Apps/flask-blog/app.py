from flask import Flask
from models.post import Post
from common.database import Database

# Database.initialize()
app = Flask(__name__)



@app.route('/')  # www.mysite.come/api/
def hello_method():
    return "Hello world"


post = Post(blog_id="123",
            title="Another great post",
            content="This is some test contest",
            author="Ira")


print(post.author)
print(post.title)
print(post.created_date)


if __name__ == '__main__':
    app.run(port=1000)








