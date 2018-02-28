from database import Database
from models.post import Post

Database.initialize()

blog=Blog(author="Ira",
          title="Something
          description="Sample")


blog.new_post()

blog.save_to_mongo()

blog.from_mongo()

blog.get_posts() #Post.fron_blog (id)
