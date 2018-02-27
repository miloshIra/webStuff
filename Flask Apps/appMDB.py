from database import Database
from models.post import Post

Database.initialize()

post=Post("Post1 title", "Post1 content", "Post1 author")
post2=Post("Post2 title", "Post2 content", "Post2 author")

print(post.content)
print(post2.content)
