from common.database import Database
from models.blog import Blog


class Menu:
    def __init__(self):
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print(f"Welcome back {self.user}")
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.get_from_mongo(blog['id'])
            return True
        else:
            pass

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to read (R) or write (W) blogs? ")
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blogs()

        elif read_or_write == 'W':
            self.user_blog.new_post()

        else:
            print("Thank you for blogging")

    def _prompt_write_post(self):
        self.user_blog.new_post()

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})
        for blog in blogs:
            print(f"ID: {blog['id']}, Title: {blog['title']}, Author {blog['author']}")

    def _view_blogs(self):
        bolg_to_see = input("Enter the ID of the blog you would like to see ")
        blog = Blog.get_from_mongo(bolg_to_see)
        posts = blog.get_posts()
        for post in posts:
            print(f"Date: {post['created_date']}\n,"
                  f"Title: {post['title']}\n"
                  f"{post['content']}")
