import pymongo
from flask import Flask
from common.database import Database
from models.post import Post
from models.blog import Blog
from menu import Menu

Database.initialize()
menu = Menu()
menu.run_menu()

# blog = Blog(author="Ira",
#             title="Sample title",
#             description="This is not so great")
#
# blog.new_post()
#
# blog.save_to_mongo()
#
# from_database = Blog.get_from_mongo(blog.id)
#
# print(blog.get_posts())

# app = Flask()
#
# @app.route('/')
# def hello_method():
#     return "Hello world"
#
#
# students = collection.find_one({}, )
#
#
# if __name__ == "__main__":
#     app.run(port=1000)
