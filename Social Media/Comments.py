from typing import Dict, List
import Users
import Posts


class Comment:
    def __init__(self,user:Users.User,post:Posts.Post,content:str):
        self.user = user
        self.post = post
        self.content = content
        self.comments:Dict[Users.User,List[Comment]] = {}

    def add_comment(self,user):
        if user not in self.comments:
            self.comments[user] = [self]
        else:
            self.comments[user].append(self)

    def view_comments(self):
        for user, comm in self.comments.items():
            print(user.name,'-->',[i.content for i in comm])