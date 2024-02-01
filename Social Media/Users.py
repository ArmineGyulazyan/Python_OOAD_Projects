
class User:
    def __init__(self,name:str,contact:str):
        self.name = name
        self.contact = contact
        self.posts = []


    def view_posts(self):
        for post in self.posts:
            print(post.content)