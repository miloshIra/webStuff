from database import Database
from models.blog import Blog

Database.initialize()

blog=Blog(author="Ira",
          title="Something",
          description="Sample")


blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts()) #Post.fron_blog (id)
