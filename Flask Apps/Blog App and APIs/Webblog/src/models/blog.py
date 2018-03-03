import uuid
import datetime
from src.models.post import Post
from src.common.database import Database


class Blog():
    def __init__(self, author, title, description, _id=None):
        self.author = author
        self.title = title
        self.description = description
    self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date, or leave blank for today (in format DDMMYYYY): ")
        if date == "":
            date = datetime.datetime.now()
        else:
            date = datetime.datetime.strptime(date,"%d%m%Y")
        post = Post(blog_id =self._id,
                    author = self.author,
                    title = title,
                    content = content,
                    created_date = date)

        post.save_to_mongo()


    def get_posts(self):
        return Post.from_blog(self.id)


    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        return {
            'author':self.author,
            'title':self.title,
            'description':self.description,
            '_id':self._id
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data=Database.find_one(collection='blogs', query={'_id':id})

        return cls(**blog_data)
